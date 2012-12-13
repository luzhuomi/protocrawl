
from pysolr import * # easy_install pysolr


def validate(doc):
    return True


class InvalidDocException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class PIndexManager():
    conn = None
    def __init__(self,url='http://127.0.0.1:8983/solr'):
        self.conn = Solr(url)
        
    def search(self,q):
        results = self.conn.search(q)
        return results

    def get_conn(self):
        return self.conn

    def del_all(self):
        self.conn.delete(q='*:*')



class PIndex():
    doc = None
    def __init__(self,doc):
        if validate(doc):
            self.doc = doc
        else:
            raise InvalidDocException("the doc is invalid, %s" %s (str(doc)))
    def save(self,url='http://127.0.0.1:8983/solr'):
        conn = Solr(url)
        conn.add([self.doc])

    objects = PIndexManager()


