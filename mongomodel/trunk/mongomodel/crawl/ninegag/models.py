from mongoengine import *


def init(host='127.0.0.1',username='nypuser',password='p455w0rd'):
	''' initialize the connection and return a DB object '''
	DBNAME='crawl_ninegag'
	db = connect(DBNAME,host=host,username=username,password=password)
	db.slave_ok = True
	return db

class Article(Document):
	url = StringField(required=True)
	author_id = StringField(required=True)
	body = StringField()
	title = StringField()
	date_posted = DateTimeField(required=True)
	image = StringField()
	meta = {
		'indexes': ['url', 'author_id', 'date_posted', 'title'],
	}

	def to_doc(self):
		doc = {}
		doc['url'] = self.url
		doc['author_id'] = self.author_id
		doc['body'] = self.body
		doc['title'] = self.title
		doc['date_posted'] = self.date_posted
		doc['image'] = self.image if self.image[0:5] == "http:" else "http:" + self.image
		doc['id'] = self.id
		return doc


