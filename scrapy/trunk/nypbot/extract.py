import re

from scrapy.link import Link
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup

import lxml.html as lxml


## BeautifulSoup can't fix <! problem correctly
class SoupLinkExtractor(object):
    def __init__(self, *args, **kwargs):
        super(SoupLinkExtractor, self).__init__()
        allow_re = kwargs.get('allow', None)
        self._allow = re.compile(allow_re) if allow_re else None
    
    def extract_links(self, response):
        raw_follow_urls = []
        
        soup = BeautifulSoup(response.body_as_unicode())
        #print soup
        anchors = soup.findAll('a')
        #print len(anchors)
        for anchor in anchors:
            anchor_href = anchor.get('href', None)
            if anchor_href and not anchor_href.startswith('#'):
                raw_follow_urls.append(anchor_href)
                
        potential_follow_urls = [urljoin(response.url, raw_follow_url) for raw_follow_url in raw_follow_urls]
        #print len(potential_follow_urls)
        if self._allow:
            follow_urls = [potential_follow_url for potential_follow_url in potential_follow_urls if self._allow.search(potential_follow_url) is not None]
        else:
            follow_urls = potential_follow_urls
            
        return [Link(url = follow_url) for follow_url in follow_urls]



class LxmlLinkExtractor:

    def __init__(self, *args, **kwargs):
        allow_re = kwargs.get('allow', None)
        deny_re = kwargs.get('deny', None)
        self._allow = re.compile(allow_re) if allow_re else None
        self._deny  = re.compile(deny_re) if deny_re else None

    def extract_links(self, response):
        raw_follow_urls = []
        
        tree = lxml.fromstring(response.body)
        # links = tree.xpath('a/@href') # of type lxml.etree._ElementStringResult
        for link in tree.iterdescendants('a'):
            if link.attrib.has_key('href'):
                raw_follow_urls.append(link.attrib['href'])

        potential_follow_urls = [urljoin(response.url, raw_follow_url) for raw_follow_url in raw_follow_urls]
        #print len(potential_follow_urls)
        if self._allow:
            follow_urls = [potential_follow_url for potential_follow_url in potential_follow_urls if self._allow.search(potential_follow_url) is not None]
        else:
            follow_urls = potential_follow_urls

        if self._deny:
            filtered_follow_urls = [url for url in follow_urls if self._deny.search(url) is None]
        else:
            filtered_follow_urls = follow_urls
            
        return [Link(url = follow_url) for follow_url in filtered_follow_urls]
            
            
        return links

    
