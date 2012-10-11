import twitter
from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo

CONSUMER_KEY='Vp0UrPOKfUDonEn4B5RCpg'
CONSUMER_SECRET='3wdvhsj1ph2PiNi1E47XullWsaEEZpepMPh4bgOCMY'
ACCESS_TOKEN_KEY='634391884-qFKI6JYrZV6JFQYHIFhConcn7S1Se86SP0YHHWDt'
ACCESS_TOKEN_SECRET='zcUKICiN4GWYrS7cyOBHyiJCHqeyjMGn3J7GfwVWrZ8'


def get_status(api,screenname):
    for p in range(1,21):
        statuses = api.GetUserTimeline(screenname,page=p)
        if len(statuses) > 0:
            user = statuses[0].user
            exists = User.objects.filter(uid = user.id)
            if exists:
                print "user exists"
                u = exists[0]
                pass
            else:
                u = User(uid = user.id, name = user.name)
                u.favourites_count = user.favourites_count
                u.favorites_count = user.friends_count
                u.following = user.following
                u.followers_count = user.followers_count
                u.profile_image_url = user.profile_image_url
                u.contributors_enabled = user.contributors_enabled
                u.geo_enabled = user.geo_enabled
                u.created_at = parse(user.created_at)
                u.description = user.description
                u.listed_count = user.listed_count
                u.follow_request_sent = user.follow_request_sent
                u.time_zone = user.time_zone
                u.url = user.url
                u.verified = user.verified
                u.default_profile = user.default_profile
                u.show_all_inline_media = user.show_all_inline_media
                u.is_translator = user.is_translator
                u.notifications = user.notifications
                u.protected = user.protected
                u.location = user.location
                u.statuses_count = user.statuses_count
                u.default_profile_image = user.default_profile_image
                u.lang = user.lang
                u.utc_offset = user.utc_offset
                u.screen_name = user.screen_name
                u.save()
            for status in statuses:
                exists = Tweet.objects.filter(tid = status.id)
                if exists:
                    print "tweet exists"
                    pass
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
                    t.entities = status.entities
                    t.save()
                print status.text
        
def main():
    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_SECRET)
    users=['luzm']
    for user in users:
        get_status(api,user)

"""
>>> dir(statuses[0])
['AsDict', 'AsJsonString', 'GetContributors', 'GetCoordinates', 'GetCreatedAt', 'GetCreatedAtInSeconds', 'GetFavorited', 'GetGeo', 'GetId', 'GetInReplyToScreenName', 'GetInReplyToStatusId', 'GetInReplyToUserId', 'GetLocation', 'GetNow', 'GetPlace', 'GetRelativeCreatedAt', 'GetRetweetCount', 'GetRetweeted', 'GetRetweeted_status', 'GetSource', 'GetText', 'GetTruncated', 'GetUser', 'NewFromJsonDict', 'SetContributors', 'SetCoordinates', 'SetCreatedAt', 'SetFavorited', 'SetGeo', 'SetId', 'SetInReplyToScreenName', 'SetInReplyToStatusId', 'SetInReplyToUserId', 'SetLocation', 'SetNow', 'SetPlace', 'SetRetweetCount', 'SetRetweeted', 'SetRetweeted_status', 'SetSource', 'SetText', 'SetTruncated', 'SetUser', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_contributors', '_coordinates', '_created_at', '_favorited', '_geo', '_id', '_in_reply_to_screen_name', '_in_reply_to_status_id', '_in_reply_to_user_id', '_location', '_now', '_place', '_retweet_count', '_retweeted', '_retweeted_status', '_source', '_text', '_truncated', '_user', 'contributors', 'coordinates', 'created_at', 'created_at_in_seconds', 'favorited', 'geo', 'hashtags', 'id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'location', 'now', 'place', 'relative_created_at', 'retweet_count', 'retweeted', 'retweeted_status', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
"""


if __name__ == "__main__":
  main()
