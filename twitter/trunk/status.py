import twitter # easy_install python-twitter
from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo
import sys

from common.utils import *

def get_status(api,screenname):
    for p in range(1,21):
        try:
            statuses = api.GetUserTimeline(screenname,page=p)
            if len(statuses) > 0:
                user = statuses[0].user
                exists = User.objects.filter(uid = user.id)
                if exists:
                    print "user exists"
                    u = exists[0]
                else:
                    print(user.AsDict())
                    u = User(uid = user.id, name = user.name)
                    u.favourites_count = user.favourites_count
                    u.favorites_count = user.friends_count
                    if hasattr(user, 'following'):
                        u.following = user.following
                    u.followers_count = user.followers_count
                    u.profile_image_url = user.profile_image_url
                    u.contributors_enabled = user.contributors_enabled
                    u.geo_enabled = user.geo_enabled
                    u.created_at = parse(user.created_at)
                    u.description = user.description
                    u.listed_count = user.listed_count
                    if hasattr(user, 'follow_request_sent'):                
                        u.follow_request_sent = user.follow_request_sent
                    u.time_zone = user.time_zone
                    u.url = user.url
                    u.verified = user.verified
                    if hasattr(user, 'default_profile'):                
                        u.default_profile = user.default_profile
                    if hasattr(user, 'show_all_inline_media'):
                        u.show_all_inline_media = user.show_all_inline_media
                    if hasattr(user, 'is_translator'):
                        u.is_translator = user.is_translator
                    u.notifications = user.notifications
                    u.protected = user.protected
                    u.location = user.location
                    u.statuses_count = user.statuses_count
                    if hasattr(user, 'default_profile_image'):
                        u.default_profile_image = user.default_profile_image
                    u.lang = user.lang
                    u.utc_offset = user.utc_offset
                    u.screen_name = user.screen_name
                    u.save()
                for status in statuses:
                    exists = Tweet.objects.filter(tid = status.id)
                    if exists:
                        print "tweet exists"
                    else:            
                        t = Tweet(tid = status.id)
                        t.user = u
                        t.contributors = status.contributors
                        t.place = status.place
                        t.in_reply_to_screen_name = status.in_reply_to_screen_name
                        t.text = status.text
                        t.favorited = status.favorited
                        t.coordinates = status.coordinates
                        t.geo = status.geo
                        t.retweet_count = status.retweet_count
                        t.created_at = parse(status.created_at)
                        t.source = status._source
                        t.in_reply_to_user_id = status.in_reply_to_user_id
                        t.in_reply_to_status_id = status.in_reply_to_status_id
                        t.retweeted = status.retweeted
                        t.truncated = status.truncated
                        # t.entities = status.entities
                        t.save()
                        print status.text
        except twitter.TwitterError,e:
            print "twitter error!"
        
def main():
    cred = read_cred(sys.argv[1])        
    api = twitter.Api(
        consumer_key=cred['consumer_key'],
        consumer_secret=cred['consumer_secret'],
        access_token_key=cred['access_token_key'],
        access_token_secret=cred['access_token_secret'])
    user_file = open(sys.argv[2],'r')
    users=[]
    for ln in user_file:
        users = users + ln.strip('\r\n').split(',')
    db = init()
    for user in users:
        get_status(api,user)
    if pymongo.version == '2.0.1':
        db.connection.disconnect()
    else:
        db.disconnect()    

"""
>>> dir(statuses[0])
['AsDict', 'AsJsonString', 'GetContributors', 'GetCoordinates', 'GetCreatedAt', 'GetCreatedAtInSeconds', 'GetFavorited', 'GetGeo', 'GetId', 'GetInReplyToScreenName', 'GetInReplyToStatusId', 'GetInReplyToUserId', 'GetLocation', 'GetNow', 'GetPlace', 'GetRelativeCreatedAt', 'GetRetweetCount', 'GetRetweeted', 'GetRetweeted_status', 'GetSource', 'GetText', 'GetTruncated', 'GetUser', 'NewFromJsonDict', 'SetContributors', 'SetCoordinates', 'SetCreatedAt', 'SetFavorited', 'SetGeo', 'SetId', 'SetInReplyToScreenName', 'SetInReplyToStatusId', 'SetInReplyToUserId', 'SetLocation', 'SetNow', 'SetPlace', 'SetRetweetCount', 'SetRetweeted', 'SetRetweeted_status', 'SetSource', 'SetText', 'SetTruncated', 'SetUser', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_contributors', '_coordinates', '_created_at', '_favorited', '_geo', '_id', '_in_reply_to_screen_name', '_in_reply_to_status_id', '_in_reply_to_user_id', '_location', '_now', '_place', '_retweet_count', '_retweeted', '_retweeted_status', '_source', '_text', '_truncated', '_user', 'contributors', 'coordinates', 'created_at', 'created_at_in_seconds', 'favorited', 'geo', 'hashtags', 'id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'location', 'now', 'place', 'relative_created_at', 'retweet_count', 'retweeted', 'retweeted_status', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
"""


if __name__ == "__main__":
  main()
