from scrapy.item import Item, Field

class NypbotItem(Item):

    author_id = Field()
    body  = Field()
    title = Field()


class Post(NypbotItem):

    url = Field()
    date_posted = Field()
    def __str__(self):
        return "Website: author_id=%s title=%s body=%s url=%s date_posted=%s" % (self.get('author_id'), self.get('title'), self.get('body'), self.get('url'), self.get('date_posted'))


class PostWithPermaLink(Post):
    perma_link = Field()
    def __str__(self):
        return "Website: author_id=%s title=%s body=%s url=%s date_posted=%s perma_link=%s" % (self.get('author_id'), self.get('title'), self.get('body'), self.get('url'), self.get('date_posted'), self.get('perma_link'))
    
