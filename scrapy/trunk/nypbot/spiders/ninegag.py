from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from nypbot.items import PostWithImage
from nypbot.utils import normalizeFriendlyDate

# from mongomodel.crawl.ninegag.models import * 

from dateutil.parser import parse
import pymongo



class NineGagSpider(CrawlSpider):
    name = "ninegag"
    allowed_domains = ["9gag.com"]
    start_urls = [
        "http://9gag.com/"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=('9gag.com/gag/\d+', )), callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        posts = hxs.select("//div[@id='main']/div[@id='block-content']")
        items = []

        for post in posts:
            item = PostWithImage()
            item['author_id'] = ''.join(post.select(".//div[@class='post-info-pad']/p/a/text()").extract())
            item['url'] = response.url
            item['body'] = ''
            item['title'] = '\n'.join(map(lambda x:x.strip('\t\n\r'),post.select(".//div[@class='post-info-pad']/h1/text()").extract()))
            item['date_posted'] = ''.join(map(lambda x:x.strip(' \t\n\r#').strip(),post.select(".//div[@class='post-info-pad']/p/text()").extract())) # todo: deal with Today and Yesterday
            item['image'] = ''.join(post.select(".//div[@class='img-wrap']/img/@src").extract())
            items.append(item)
            print item
        # self.insert_posts(items)
        return items
