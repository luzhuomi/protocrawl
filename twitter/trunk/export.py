import json
import urllib2, sys, sets

from mongomodel.crawl.twitter.models import *

import pymongo,sys

from common.utils import *

def export(user_ids, filename):
    db = init()
    users = User.objects.filter(uid__in = user_ids)
    tweets = Tweet.objects.filter(user__in = users).order_by("created_at")
    f_out = open(filename,'w')
    for t in tweets:
        ln = "\t".join([str(t.created_at), str(t.user.uid),t.user.screen_name.encode('utf-8'),t.text.encode('utf-8').replace('\r',' ').replace('\n',' ').replace('\t',' ')])
        print >> f_out, ln
            

    if pymongo.version == '2.0.1':
        db.connection.disconnect()
    else:
        db.disconnect()

    
def main():
    user_ids = get_userids_file(sys.argv[1])
    export(user_ids, sys.argv[2])



if __name__ == "__main__":
    main()
