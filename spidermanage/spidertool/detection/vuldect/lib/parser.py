#!/usr/bin/env python
# encoding: utf-8


from lxml import etree
from urlparse import urljoin

class HTMLParser(object):
    def __init__(self):
        self.parser = etree.HTMLParser()

    def parse(self, html):
        return etree.fromstring(html, self.parser)

    def findall(self, root, name='*', attrs={}):
        if not name:
            name = '*'
        if attrs:
            attr_path = '[' + '|'.join(['@' + key for key in attrs]) + ']'
        else:
            attr_path = ''
        path = './/%s%s' % (name, attr_path)
        ret = []
        elements = root.xpath(path)
        for element in elements:
            if not attrs:
                ret.append(element)
                continue
            for key, value in attrs.items():
                attr = element.attrib.get(key)
                if not attr:
                    continue
                if hasattr(value, 'match') and value.search(attr):
                    ret.append(element)
                elif value :
                    ret.append(element)
        return ret

    def get_links(self, url, root):
        urls = set()
        for elem in self.findall(root, 'a', {'href': True}):
            path = elem.attrib['href'].strip()
            if path.startswith(('#', 'javascript:', 'mailto:')):
                continue
            urls.add(urljoin(url, path))
        return urls
