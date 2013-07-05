import json
import urllib2, sys, sets

from mongomodel.crawl.twitter.models import *

import pymongo,sys

from common.utils import *

def export(keyword, filename):
    db = init()
    tweets = Tweet.objects.filter(text__icontains = keyword)
    f_out = open(filename,'w')
    for t in tweets:
        ln = "\t".join([str(t.created_at), str(t.user.uid),t.user.screen_name.encode('utf-8'),t.text.encode('utf-8').replace('\r',' ').replace('\n',' ').replace('\t',' ')])
        print >> f_out, ln
            

    if pymongo.version == '2.0.1':
        db.connection.disconnect()
    else:
        db.disconnect()

    
def main():
    keyword=sys.argv[1]
    export(keyword, sys.argv[2])



if __name__ == "__main__":
    main()
