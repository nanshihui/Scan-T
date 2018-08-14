#!/usr/bin/env python
# encoding: utf-8


from xml.dom.minidom import parseString
from urlparse import urljoin

class Sitemap(object):
    def __init__(self, func):
        self.request = func
        self.urls = set()
        self.sitemaps = set()

    def parse(self, url, text):
        try:
            dom = parseString(text)
        except:
            return
        for sitemap in dom.getElementsByTagName('sitemap'):
            locs = sitemap.getElementsByTagName('loc')
            if locs:
                try:
                    sitemap = locs[0].firstChild.data
                    self.sitemaps.add(sitemap)
                except:
                    pass
        for _url in dom.getElementsByTagName('url'):
            locs = _url.getElementsByTagName('loc')
            if locs:
                try:
                    _url = urljoin(url, locs[0].firstChild.data)
                    self.urls.add(_url)
                except:
                    pass

    def entry(self, url):
        resp = self.request(url)
        if resp == None:
            return []

        self.parse(url, resp.text)
        if resp.headers['content-type'] == 'text/plain':
            for url in resp.text.split('\n'):
                self.urls.add(url.strip())
            return self.urls
        elif 'xml' in resp.headers['content-type']:
            if not self.sitemaps:
                return self.urls
            while len(self.sitemaps):
                url = self.sitemaps.pop()
                resp = self.request(url)
                self.parse(url, resp.text)
            return self.urls

