import twitter # easy_install python-twitter
from dateutil.parser import parse
#from mongomodel.crawl.twitter.models import *
#import pymongo
import sys
from sets import *

from common.utils import *
from common.user import *

def finder(api,user_name,query):
    try:
        friends = api.GetFriends(user_name)
        candidates = []
        for friend in friends:
            if query in map(lambda w:w.strip('.,?"\':'), friend.description.lower().split(' ')):
                candidates.append(friend.screen_name)
            else:
                print "%s: profile not matched: %s" % (user_name, friend.screen_name)
        return candidates
    except twitter.TwitterError,e:
        return []

def main():
    cred = read_cred(sys.argv[1])        
    api = twitter.Api(
        consumer_key=cred['consumer_key'],
        consumer_secret=cred['consumer_secret'],
        access_token_key=cred['access_token_key'],
        access_token_secret=cred['access_token_secret']
        )

    user_file      = sys.argv[2]
    profile_query  = sys.argv[3]
    output_file    = open(sys.argv[4],'w')
    users          = read_usernames_from_file(user_file)
    known_user_set = Set(users)

    to_be_processed = list(users)
    

    while (len(to_be_processed)):
        user = to_be_processed[0]
        del to_be_processed[0]
        candidates = filter(lambda c:(c not in known_user_set), finder(api,user,profile_query))
        to_be_processed = to_be_processed + candidates
        for c in candidates:
            known_user_set.add(c)
        print >> output_file, user


if __name__ == "__main__":
  main()
