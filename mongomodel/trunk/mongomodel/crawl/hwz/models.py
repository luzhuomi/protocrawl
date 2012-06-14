
from mongoengine import *

DBNAME='crawl_hwz'

def init(host='127.0.0.1',username='nypuser',password='p455w0rd'):
	''' initialize the connection and return a DB object '''
	db = connect(DBNAME,host=host,username=username,password=password)
	db.slave_ok = True
	return db


class Post(Document):
	url = StringField(required=True)
	author_id = StringField(required=True)
	body = StringField()
	title = StringField()
	date_posted = DateTimeField(required=True)
	
	meta = {
		'indexes': ['url', 'author_id', 'date_posted'],
		}


