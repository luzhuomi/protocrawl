
import pysolor # easy_install pysolr


def validate(doc):
    return True


class InvalidDocException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class PIndex():
    doc = null
    def __init__(self,doc):
        if validate(doc):
            self.obj = obj
        else:
            raise InvalidDocException("the doc is invalid, %s" %s (str(doc)))
    def save(self):
        conn = Solr('http://127.0.0.1:8931/solr')
        conn.add(doc)

    objects = PIndexManager()


class PIndexManager():
    conn = null
    def __init__(self):
        self.conn = Solr('http://127.0.0.1:8983/solr/')
        
    def search(self,q):
        results = self.conn.search(p)
        return results

    def get_conn(self):
        return self.conn
        
