from mongoengine import *


def init(host='127.0.0.1',username='nypuser',password='p455w0rd'):
	''' initialize the connection and return a DB object '''
	DBNAME='crawl_twitter_stream'
	db = connect(DBNAME,host=host,username=username,password=password)
	db.slave_ok = True
	return db


'''
{"in_reply_to_status_id_str":null,"contributors":null,"place":null,"in_reply_to_screen_name":null,"text":"Test","favorited":false,"in_reply_to_user_id_str":null,"coordinates":null,"geo":null,"retweet_count":0,"created_at":"Fri Jul 13 09:38:00 +0000 2012","source":"web","in_reply_to_user_id":null,"in_reply_to_status_id":null,"retweeted":false,"id_str":"223712876576260096","truncated":false,"user":{"favourites_count":10,"friends_count":42,"profile_background_color":"C6E2EE","following":null,"profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme2\/bg.gif","followers_count":38,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","contributors_enabled":false,"geo_enabled":false,"created_at":"Tue Sep 23 03:08:29 +0000 2008","profile_sidebar_fill_color":"DAECF4","description":"Circos.com, Computer Science, Phd, National University of Singapore","listed_count":1,"follow_request_sent":null,"time_zone":"Singapore","url":"http:\/\/sites.google.com\/site\/luzhuomi\/","verified":false,"profile_sidebar_border_color":"C6E2EE","default_profile":false,"show_all_inline_media":false,"is_translator":false,"notifications":null,"profile_use_background_image":true,"protected":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","location":"Singapore","id_str":"16414559","profile_text_color":"663B12","name":"Kenny","statuses_count":199,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme2\/bg.gif","id":16414559,"default_profile_image":false,"lang":"en","utc_offset":28800,"profile_link_color":"1F98C7","screen_name":"luzm"},"id":223712876576260096,"entities":{"user_mentions":[],"urls":[],"hashtags":[]}}

'''


class User(Document):
	favourites_count = IntField()
	friends_count = IntField()
	#profile_background_color = StringField()
	following = StringField()
	#profile_background_tile = BooleanField()
	#profile_background_image_url_https = StringField()
	followers_count = IntField()
	profile_image_url = StringField()
	contributors_enabled = BooleanField()
	geo_enabled = BooleanField()
	created_at  = DateTimeField()
	#profile_sidebar_fill_color = StringField()
	description = StringField()
	listed_count = IntField()
	follow_request_sent = IntField()
	time_zone = StringField()
	url = StringField()
	verified = BooleanField()
	#profile_sidebar_border_color = StringField()
	default_profile = BooleanField()
	show_all_inline_media = BooleanField()
	is_translator = BooleanField()
	notifications = StringField()
	#profile_use_background_image = BooleanField()
	protected = BooleanField()
	#profile_image_url_https = StringField()
	location = StringField()
	#profile_text_color = StringField()
	name = StringField(required=True)
	statuses_count = IntField()
	#profile_background_image_url = StringField()
	uid = IntField(required=True,unique=True)
	default_profile_image = BooleanField()
	lang = StringField()
	utc_offset = IntField()
	#profile_link_color = StringField()
	screen_name = StringField(required=True)
	meta = {
		'indexes' : ['uid','screen_name'],
	}

class Tweet(Document):
	#in_reply_to_status_id_str = StringField()
	contributors = StringField()
	place = DictField()
	in_reply_to_screen_name = StringField()
	text = StringField()
	favorited = BooleanField()
	#in_reply_to_user_id_str = StringField()
	coordinates = DictField()
	geo = DictField()
	retweet_count = IntField()
	created_at = DateTimeField(required=True)
	source = StringField()
	in_reply_to_user_id = IntField()
	in_reply_to_status_id = IntField()
	retweeted = BooleanField()
	#id_str = StringField()
	truncated = BooleanField()
	user = ReferenceField(User)
	tid = IntField(unique=True,required=True)
	entities = DictField()
	meta = {
		'indexes': ['tid', 'created_at', ],
	}



class E(EmbeddedDocument):
	ef = StringField()

class R(Document):
	rf = StringField()

class T(Document):
	e = EmbeddedDocumentField(E)
	r = ReferenceField(R)


''' the profile 
class ProfileGroup(Document):
	name = StringField(unique=True,required=True)
	profile_keywords = DictField()
	meta = {
		'indexes': ['name']
		}

class ProfileGroupUser(Document):
	user = ReferenceField(User)
	profile_group = ReferenceField(Profile)
	meta = {
		'indexes' : ['profile_group', 'user']
		}

'''


class ScreenNameCache(model):
	screenname = StringField()
	tid = StringField()
	meta = {
		'indexes' : ['screenname']
		}
	
