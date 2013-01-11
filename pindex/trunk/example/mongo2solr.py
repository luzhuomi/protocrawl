import sys
import mongomodel.crawl.ninegag.models as m
import pindex.index as i
import pymongo

def main():
    db = m.init()
    i.PIndex.objects.del_all()
    for o in m.Article.objects.all():
        d = o.to_doc()
        pi = i.PIndex(d)
        # d['body'] = 'http://'
        del d['image']
        del d['author']
        del d['date_posted']
        print (d)
        pi.save()
    db.close()
    if pymongo.version == '2.0.1':
        db.connection.disconnect()
    else:
        db.disconnect()

if __name__ == "__main__":
    sys.exit(main())    
