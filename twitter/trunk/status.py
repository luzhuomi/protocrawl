#import twitter # easy_install python-twitter
from time import sleep
from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo
import sys

from common.utils import *
from common.user import mk_user_obj,read_usernames_from_file
from twython import Twython, TwythonError

def get_status(twitter,screenname):
    lastid = None
    currid = None
    while (currid is None or currid != lastid):
        lastid = currid
        try:
            print (lastid, currid)
            statuses = twitter.get_user_timeline(screen_name=screenname, max_id=currid,count=200) if currid else twitter.get_user_timeline(screen_name=screenname)
            if len(statuses) > 0:
                user = statuses[0]['user']
                u = mk_user_obj(user)
                for status in statuses:
                    currid = status['id']
                    exists = Tweet.objects.filter(tid = status['id'])
                    if exists:
                        print "tweet exists"
                    else:            
                        t = Tweet(tid = status['id'])
                        t.user = u
                        t.contributors = status['contributors']
                        t.place = status['place']
                        t.in_reply_to_screen_name = status['in_reply_to_screen_name']
                        t.text = status['text']
                        t.favorited = status['favorited']
                        t.coordinates = status['coordinates']
                        t.geo = status['geo']
                        t.retweet_count = status['retweet_count']
                        t.created_at = parse(status['created_at'])
                        t.source = status['source']
                        t.in_reply_to_user_id = status['in_reply_to_user_id']
                        t.in_reply_to_status_id = status['in_reply_to_status_id']
                        t.retweeted = status['retweeted']
                        t.truncated = status['truncated']
                        # t.entities = status.entities
                        t.save()
                        print status['text']
            sleep(60)
        except Exception as e:
            print "twitter error!" + (str(e))
        
def main():
    cred = read_cred(sys.argv[1])
    user_file = sys.argv[2]
    users = read_usernames_from_file(user_file)
    
    twitter = Twython(cred['consumer_key'], cred['consumer_secret'],
                    cred['access_token_key'], cred['access_token_secret'])
    db = init()
    for user in users:
        get_status(twitter,user)
    if hasattr(db,'disconnect'):
        db.disconnect()
    else:
        db.connection.disconnect()




if __name__ == "__main__":
  main()
