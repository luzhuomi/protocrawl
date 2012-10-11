from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from nypbot.items import Post
from nypbot.utils import normalizeFriendlyDate

from mongomodel.crawl.hwz.models import * # apparently, scrapy does not like a class named 'Post' :(

from dateutil.parser import parse
import pymongo

class HwzSpider(CrawlSpider):
    name = "hwztravel"
    allowed_domains = ["hardwarezone.com.sg"]
    start_urls = [
        "http://forums.hardwarezone.com.sg/travel-accommodation-89/",
        "http://forums.hardwarezone.com.sg/malaysia-269/",
        "http://forums.hardwarezone.com.sg/thailand-279/",
        "http://forums.hardwarezone.com.sg/korea-283/",
        "http://forums.hardwarezone.com.sg/taiwan-291/",
        "http://forums.hardwarezone.com.sg/china-trial-316/",
        "http://forums.hardwarezone.com.sg/australia-trial-317/",
        "http://forums.hardwarezone.com.sg/hong-kong-270/",
        "http://forums.hardwarezone.com.sg/japan-271/",
        "http://forums.hardwarezone.com.sg/europe-277/",
    ]
    rules = (
        # Extract links matching 'garage-sales-18/.*html' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('travel\-accommodation\-89/.*\.html', )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('malaysia\-269/.*\.html', )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('thailand\-279/.*\.html', )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('korea\-283/.*\.html', )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('taiwan\-291/.*\.html', )), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('china\-trial\-316/.*\.html', )), callback='parse_item', follow=True),        
        Rule(SgmlLinkExtractor(allow=('australia\-trial\-317/.*\.html', )), callback='parse_item', follow=True),        
        Rule(SgmlLinkExtractor(allow=('hong\-kong\-270/.*\.html', )), callback='parse_item', follow=True),        
        Rule(SgmlLinkExtractor(allow=('japan\-271/.*\.html', )), callback='parse_item', follow=True),        
        Rule(SgmlLinkExtractor(allow=('europe\-277/.*\.html', )), callback='parse_item', follow=True),        

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )


    def insert_posts(self,posts):
        db = init()
        
        for item in posts:
            art = Message(forum = self.name,
                          url=item.get('url'),
                          author_id=item.get('author_id'),
                          body=item.get('body'),
                          title=item.get('title'),
                date_posted=parse(normalizeFriendlyDate(item.get('date_posted'))))
            rs = Message.objects.filter(forum = self.name, author_id = art.author_id, url= art.url, date_posted = art.date_posted)
            if len(rs) == 0:
                try: 
                    art.save()
                except UnicodeEncodeError,e:
                    self.log("unicode encode error")
                except Exception,e:
                    self.log("Error:")
                    self.log(e.message)
            else:
                self.log("article exists")
        if pymongo.version == '2.0.1':
            db.connection.disconnect()
        else:
            db.disconnect()
	
    """
    When writing crawl spider rules, avoid using parse as callback, since the CrawlSpider uses the parse method itself to implement its logic. So if you override the parse method, the crawl spider will no longer work.
    """

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        posts = hxs.select("//div[@id='posts']/div[@class='post-wrapper']")
        items = []

        for post in posts:
            item = Post()
            item['author_id'] = ''.join(post.select(".//a[@class='bigusername']/text()").extract())
            item['url'] = response.url
            item['body'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select(".//td[@class='alt1']/div/text()").extract()))
            item['title'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select("//h2[@class='header-gray']/text()").extract()))
            item['date_posted'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//td[@class='thead']/text()").extract())) # todo: deal with Today and Yesterday
            # item['date_posted'] = normalizeFriendlyDate(' '.join(map(lambda x:x.strip(' \t\n\r'),post.select(".//td[@class='thead']/text()").extract()))) # todo: deal with Today and Yesterday
            items.append(item)
        self.insert_posts(items)
        return items
