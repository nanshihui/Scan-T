#!/usr/bin/env python
# encoding: utf-8


from urlparse import urljoin

class Robots(object):
    def __init__(self, func):
        self.request = func
        self.urls = set()
        self.sitemaps = set()

    def parse(self, url, data):
        for line in data.split('\n'):
            line = line.strip()
            if line.startswith(('Allow:', 'Disallow')):
                if '*' in line:
                    continue
                self.urls.add(urljoin(url, line.split(':', 1)[1].strip()))
            elif line.startswith('Sitemap:'):
                self.sitemaps.add(line.split(':', 1)[1])
        return self.urls, self.sitemaps

    def entry(self, url):
        resp = self.request(url)
        if resp == None:
            return [], []
        return self.parse(url, resp.text)

