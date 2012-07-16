from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from nypbot.items import Post,PostWithPermaLink
from nypbot.utils import normalizeFriendlyDate
from nypbot.extract import LxmlLinkExtractor # SoupLinkExtractor

from mongomodel.crawl.toc.models import * 

from dateutil.parser import parse
import pymongo

class TocSpider(CrawlSpider):
    name = "toc"
    allowed_domains = ["theonlinecitizen.com"]
    start_urls = [
        "http://theonlinecitizen.com/2012/",
        #"http://theonlinecitizen.com/2012/06/world-markets-rattled-by-greek-elections/",
        #"http://theonlinecitizen.com/2011/",
        #"http://theonlinecitizen.com/2010/",       
    ]
    rules = (
        # Extract links matching 'garage-sales-18/.*html' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LxmlLinkExtractor(allow=(), deny=('jpg$')), callback='extract_item', follow=True),
        #Rule(SgmlLinkExtractor(allow=('2011', )), callback='extract_item', follow=True),
        #Rule(SgmlLinkExtractor(allow=('2010', )), callback='extract_item', follow=True),        

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )


    def insert_posts(self,posts):
        db = init()
        for item in posts:
            cmt = Comment(url=item.get('url'),
                        author_id=item.get('author_id'),
                        body=item.get('body'),
                        title=item.get('title'),
                        date_posted=parse(normalizeFriendlyDate(item.get('date_posted'))),
                        perma_link=item.get('perma_link'),
                )
            rs = Comment.objects.filter(author_id = cmt.author_id, url= cmt.url, date_posted = cmt.date_posted)
            if len(rs) == 0:
                try: 
                    cmt.save()
                except UnicodeEncodeError,e:
                    self.log("unicode encode error")
                except Exception,e:
                    self.log("Error:")
                    self.log(e.message)
            else:
                self.log("comment exists")
        if pymongo.version == '2.0.1':
            db.connection.disconnect()
        else:
            db.disconnect()
	
    """
    When writing crawl spider rules, avoid using parse as callback, since the CrawlSpider uses the parse method itself to implement its logic. So if you override the parse method, the crawl spider will no longer work.
    """

    def extract_item(self, response):
        hxs = HtmlXPathSelector(response)
        posts = hxs.select("//ol[@class='commentlist']/li")
        items = []
        
        for post in posts:
            item = PostWithPermaLink()
            item['author_id'] = ''.join(post.select(".//div[@class='comment-head']/span[@class='name left']/text()").extract())
            item['url'] = response.url # todo
            item['body'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select(".//div[@class='comment-entry']/p/text()").extract()))
            item['title'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select("//h2[@class='posttitle']/text()").extract()))
            item['date_posted'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//div[@class='comment-head']/span[@class='date right']/a/text()").extract()))
            item['perma_link'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//div[@class='comment-head']/span[@class='date right']/a/@href").extract()))
            items.append(item)

        self.insert_posts(items)
        # the following does not work, toc embed fb comments in an iframe, which is triggered by ajax.
        '''
        
        fb_posts = hxs.select("//iframe//ui[@class='uiList fbFeedbackPosts']/li")


        fb_items = [] 
        for fb_post in fb_posts:
            fb_item = PostWithPermaLink()
            fb_item['author_id'] = ''.join(post.select(".//a[@class='profileName']/text()").extract())
            fb_item['url'] = response.url
            fb_item['body'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select(".//div[@class='postText']/text()").extract()))
            fb_item['title'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select("//h2[@class='posttitle']/text()").extract()))
            fb_item['date_posted'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//abbr/@title").extract()))
            fb_item['perma_link'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//a[@class='uiLinkSubtle']/@href").extract()))
        '''
        
        return items
