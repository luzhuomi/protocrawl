from mongoengine import *


def init(host='127.0.0.1',username='nypuser',password='p455w0rd'):
	''' initialize the connection and return a DB object '''
	DBNAME='crawl_toc'
	db = connect(DBNAME,host=host,username=username,password=password)
	db.slave_ok = True
	return db

class Comment(Document):
	url = StringField(required=True)
	author_id = StringField(required=True)
	body = StringField()
	title = StringField()
	date_posted = DateTimeField(required=True)
	perma_link = StringField()
	meta = {
		'indexes': ['url', 'author_id', 'date_posted', 'perma_link'],
	}


