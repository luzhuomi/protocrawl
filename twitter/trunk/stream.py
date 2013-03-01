import pycurl, json, urllib2, sys, sets
from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo

from common.utils import *

STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json?follow="

def insert_to_mongo(data):
    db = init()
    try:
        data_json = json.loads(data)
        if data_json.has_key("user"):
            user = data_json["user"]
            u = None
            if user.has_key("id") and user.has_key("name"):
                exists =  User.objects.filter(uid = user["id"])
                if exists:
                    u = exists[0]
                    print "user exists"
                else:
                    u = User(uid = user["id"], name = user["name"])
                if user.has_key("favourites_count"):
                    u.favourites_count = user["favourites_count"]
                if user.has_key("friends_count"):
                    u.favorites_count = user["friends_count"]
                if user.has_key("following"):
                    u.following = user["following"]
                if user.has_key("followers_count"):
                    u.followers_count = user["followers_count"]
                if user.has_key("profile_image_url"):
                    u.profile_image_url = user["profile_image_url"]
                if user.has_key("contributors_enabled"):
                    u.contributors_enabled = user["contributors_enabled"]
                if user.has_key("geo_enabled"):
                    u.geo_enabled = user["geo_enabled"]
                if user.has_key("created_at"):
                    u.created_at = parse(user["created_at"])
                if user.has_key("description"):
                    u.description = user["description"]
                if user.has_key("listed_count"):
                    u.listed_count = user["listed_count"]
                if user.has_key("follow_request_sent"):
                    u.follow_request_sent = user["follow_request_sent"]
                if user.has_key("time_zone"):
                    u.time_zone = user["time_zone"]
                if user.has_key("url"):
                    u.url = user["url"]
                if user.has_key("verified"):
                    u.verified = user["verified"]
                if user.has_key("default_profile"):
                    u.default_profile = user["default_profile"]
                if user.has_key("show_all_inline_media"):
                    u.show_all_inline_media = user["show_all_inline_media"]
                if user.has_key("is_translator"):
                    u.is_translator = user["is_translator"]
                if user.has_key("notifications"):
                    u.notifications = user["notifications"]
                if user.has_key("protected"):
                    u.protected = user["protected"]
                if user.has_key("location"):
                    u.location = user["location"]
                if user.has_key("statuses_count"):
                    u.statuses_count = user["statuses_count"]
                if user.has_key("default_profile_image"):
                    u.default_profile_image = user["default_profile_image"]
                if user.has_key("lang"):
                    u.lang = user["lang"]
                if user.has_key("utc_offset"):
                    u.utc_offset = user["utc_offset"]
                if user.has_key("screen_name"):
                    u.screen_name = user["screen_name"]
                u.save()
            else:
                pass

            if data_json.has_key("id") and u:
                exists = Tweet.objects.filter( tid = data_json["id"])
                if exists:
                    print "tweet exists"
                    pass
                else:
                    t = Tweet(tid = data_json["id"])
                    t.user = u
                    if data_json.has_key("contributors"):
                        t.contributors = data_json["contributors"]
                    if data_json.has_key("place"):
                        t.place = data_json["place"]
                    if data_json.has_key("in_reply_to_screen_name"):
                        t.in_reply_to_screen_name = data_json["in_reply_to_screen_name"]
                    if data_json.has_key("text"):
                        t.text = data_json["text"]
                    if data_json.has_key("favorited"):
                        t.favorited = data_json["favorited"]
                    if data_json.has_key("coordinates"):
                        t.coordinates = data_json["coordinates"]
                    if data_json.has_key("geo"):
                        t.geo = data_json["geo"]
                    if data_json.has_key("retweet_count"):
                        t.retweet_count = data_json["retweet_count"]
                    if data_json.has_key("created_at"):
                        t.created_at = parse(data_json["created_at"])
                    if data_json.has_key("source"):
                        t.source = data_json["source"]
                    if data_json.has_key("in_reply_to_user_id"):
                        t.in_reply_to_user_id = data_json["in_reply_to_user_id"]
                    if data_json.has_key("in_reply_to_status_id"):
                        t.in_reply_to_status_id = data_json["in_reply_to_status_id"]
                    if data_json.has_key("retweeted"):
                        t.retweeted = data_json["retweeted"]
                    if data_json.has_key("truncated"):
                        t.truncated = data_json["truncated"]
                    if data_json.has_key("entities"):
                        t.entities = data_json["entities"]
                    t.save()
            else:
                pass
    except ValueError,e:
        print "Value Error %s " % (data)
        # raise e


    if hasattr(db,'disconnect'):
	db.disconnect()
    else:
        db.connection.disconnect()

        

def on_receive(data):
    #data_json = json.loads(data)
    print data    
    insert_to_mongo(data)

if len(sys.argv) < 1:
    print "Usage: stream.py <user_id file>"
    sys.exit(1)

user_ids = get_userids_file(sys.argv[2])


def loop(retry):
    try:
        cred = read_cred(sys.argv[1])
        conn = pycurl.Curl()
        conn.setopt(pycurl.USERPWD, "%s:%s" % (cred['user'], cred['password']))
        conn.setopt(pycurl.URL, STREAM_URL+','.join(map(str,user_ids)))
        conn.setopt(pycurl.WRITEFUNCTION, on_receive)
        conn.perform()
    except:
        if retry > 0:
            print "="*20
            print "retrying..."
            loop(retry-1)
        else:
            print "="*20            
            print "no more retry, exiting..."
            sys.exit(0)

loop(5)
    

s1 = '{"in_reply_to_status_id_str":null,"contributors":null,"place":null,"in_reply_to_screen_name":null,"text":"Test","favorited":false,"in_reply_to_user_id_str":null,"coordinates":null,"geo":null,"retweet_count":0,"created_at":"Fri Jul 13 09:38:00 +0000 2012","source":"web","in_reply_to_user_id":null,"in_reply_to_status_id":null,"retweeted":false,"id_str":"223712876576260096","truncated":false,"user":{"favourites_count":10,"friends_count":42,"profile_background_color":"C6E2EE","following":null,"profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme2\/bg.gif","followers_count":38,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","contributors_enabled":false,"geo_enabled":false,"created_at":"Tue Sep 23 03:08:29 +0000 2008","profile_sidebar_fill_color":"DAECF4","description":"Circos.com, Computer Science, Phd, National University of Singapore","listed_count":1,"follow_request_sent":null,"time_zone":"Singapore","url":"http:\/\/sites.google.com\/site\/luzhuomi\/","verified":false,"profile_sidebar_border_color":"C6E2EE","default_profile":false,"show_all_inline_media":false,"is_translator":false,"notifications":null,"profile_use_background_image":true,"protected":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","location":"Singapore","id_str":"16414559","profile_text_color":"663B12","name":"Kenny","statuses_count":199,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme2\/bg.gif","id":16414559,"default_profile_image":false,"lang":"en","utc_offset":28800,"profile_link_color":"1F98C7","screen_name":"luzm"},"id":223712876576260096,"entities":{"user_mentions":[],"urls":[],"hashtags":[]}}'

s2 = '{"in_reply_to_status_id_str":null,"contributors":null,"place":null,"in_reply_to_screen_name":"luzm","text":"@luzm http:\/\/t.co\/0yzHGZnT #test abc","favorited":false,"in_reply_to_user_id_str":"16414559","coordinates":null,"geo":null,"retweet_count":0,"created_at":"Fri Jul 13 16:03:07 +0000 2012","source":"web","in_reply_to_user_id":16414559,"in_reply_to_status_id":null,"possibly_sensitive_editable":true,"retweeted":false,"id_str":"223809793016598528","truncated":false,"possibly_sensitive":false,"user":{"favourites_count":10,"friends_count":42,"profile_background_color":"C6E2EE","following":null,"profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme2\/bg.gif","followers_count":38,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","contributors_enabled":false,"geo_enabled":false,"created_at":"Tue Sep 23 03:08:29 +0000 2008","profile_sidebar_fill_color":"DAECF4","description":"Circos.com, Computer Science, Phd, National University of Singapore","listed_count":1,"follow_request_sent":null,"time_zone":"Singapore","url":"http:\/\/sites.google.com\/site\/luzhuomi\/","verified":false,"profile_sidebar_border_color":"C6E2EE","default_profile":false,"show_all_inline_media":false,"is_translator":false,"notifications":null,"profile_use_background_image":true,"protected":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","location":"Singapore","id_str":"16414559","profile_text_color":"663B12","name":"Kenny","statuses_count":198,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme2\/bg.gif","id":16414559,"default_profile_image":false,"lang":"en","utc_offset":28800,"profile_link_color":"1F98C7","screen_name":"luzm"},"id":223809793016598528,"entities":{"user_mentions":[{"indices":[0,5],"name":"Kenny","id_str":"16414559","id":16414559,"screen_name":"luzm"}],"urls":[{"display_url":"google.com","indices":[6,26],"url":"http:\/\/t.co\/0yzHGZnT","expanded_url":"http:\/\/www.google.com"}],"hashtags":[{"text":"test","indices":[27,32]}]}}'

s3 = '{"place":{"country":"Indonesia","place_type":"admin","url":"http:\/\/api.twitter.com\/1\/geo\/id\/992d462f77b3d1e6.json","country_code":"ID","bounding_box":{"type":"Polygon","coordinates":[[[100.093771,-1.072918],[109.165833,-1.072918],[109.165833,4.795255],[100.093771,4.795255]]]},"attributes":{},"full_name":"Riau, Indonesia","name":"Riau","id":"992d462f77b3d1e6"},"text":"Why are we being judged for the amount we tip? Especially in a luxury sector? Isn\'t the service already factored into the product?","favorited":false,"in_reply_to_status_id_str":null,"contributors":null,"coordinates":{"type":"Point","coordinates":[103.80973753,1.25758638]},"geo":{"type":"Point","coordinates":[1.25758638,103.80973753]},"in_reply_to_screen_name":null,"created_at":"Mon Jul 16 07:47:59 +0000 2012","in_reply_to_user_id_str":null,"source":"","retweet_count":0,"in_reply_to_user_id":null,"in_reply_to_status_id":null,"retweeted":false,"truncated":false,"user":{"statuses_count":8460,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme5\/bg.gif","default_profile_image":false,"profile_link_color":"D02B55","following":null,"favourites_count":4,"friends_count":163,"followers_count":185,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/2319249068\/image_normal.jpg","created_at":"Wed Apr 01 05:16:41 +0000 2009","profile_background_color":"352726","description":"This is where I let my inner bitch come out. ","profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme5\/bg.gif","time_zone":"Singapore","url":null,"contributors_enabled":false,"verified":false,"geo_enabled":true,"profile_sidebar_fill_color":"99CC33","listed_count":5,"follow_request_sent":null,"notifications":null,"profile_sidebar_border_color":"829D5E","protected":false,"location":"T: 1.309822,103.851992","default_profile":false,"show_all_inline_media":false,"name":"Rae","is_translator":false,"profile_use_background_image":true,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/2319249068\/image_normal.jpg","id":28056319,"id_str":"28056319","lang":"en","utc_offset":28800,"profile_text_color":"3E4415","screen_name":"tangrae"},"id":224772353391988736,"id_str":"224772353391988736","entities":{"urls":[],"user_mentions":[],"hashtags":[]}}'
