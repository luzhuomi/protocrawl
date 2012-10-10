from mongoengine import *


def init(host='127.0.0.1',username='nypuser',password='p455w0rd'):
	''' initialize the connection and return a DB object '''
	DBNAME='crawl_hwz'
	print DBNAME
	db = connect(DBNAME,host=host,username=username,password=password)
	db.slave_ok = True
	return db

class Article(Document): # old one, current affair is here.
	url = StringField(required=True)
	author_id = StringField(required=True)
	body = StringField()
	title = StringField()
	date_posted = DateTimeField(required=True)
	
	meta = {
		'indexes': ['url', 'author_id', 'date_posted'],
	}


class Message(Document): # new one, everything else 
	forum = StringField(required=True)
	url = StringField(required=True)
	author_id = StringField(required=True)
	body = StringField()
	title = StringField()
	date_posted = DateTimeField(required=True)
	
	meta = {
		'indexes': ['forum', 'url', 'author_id', 'date_posted'],
	}
	
