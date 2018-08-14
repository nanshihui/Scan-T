#!/usr/bin/env python
# encoding: utf-8
import urlparse
import re
from bs4 import BeautifulSoup

"""
BeautifulSoup:
encoding error : input conversion failed due to input error, bytes 0x9E 0x65 0xBA 0xD3
"""
def format_html(html,charset=''):
  def get_charset(html):
    if html[0:3] == '\xef\xbb\xbf':
      return 'UTF-8'
    match = re.search('<meta\s[\s\S]*?charset[\s]*?=[\s]*?[\'"]?([a-z0-9\-]+)[\'"]?[\s\S]*?>', html, re.IGNORECASE)
    if match:
      return match.group(1)
    return 'GB18030'

  def convert_to_unicode(content):
    if isinstance(content, str):
      try:
        return force_convert_cn(content)
      except UnicodeDecodeError as e:
        print(e)
    return content

  def force_convert_cn(content,charset=''):
    if not charset == '':
      return content.decode(charset, 'ignore')
    try_list = ["UTF-8", "GB18030", "BIG5"]
    for codec in try_list:
      try:
        decoded = content.decode(codec)
        return decoded
      except UnicodeDecodeError as e:
        continue
    charset = get_charset(content)
    decoded = content.decode(charset, 'ignore')
    return decoded

  def html_entity_decode(html):
    try:
      import HTMLParser
      parser = HTMLParser.HTMLParser()
      return parser.unescape(html)
    except:
      return html

  #html = html_entity_decode(html)
  html = convert_to_unicode(html)
  return html

class LinksParser(object):
    """docstring for link_parser"""
    def __init__(self, baseurl, html_content):
        super(LinksParser, self).__init__()
        self.weburl = self.baseurl = baseurl
        self.html_content = format_html(html_content)
        self.url_links = {
            'a':[],
            'link':[],
            'img':[],
            'script':[],
      'form':[],
      'location':[],
        }
        self.external_links = []
        self.internal_links = []
        self.soup = BeautifulSoup(self.html_content, 'lxml')
        self.get_baseurl()

    def get_baseurl(self):
        tag = self.soup.find('base')
        if tag and tag.attrs.has_key('href'):
            if not urlparse.urlparse(tag.attrs['href']).netloc == '':
                self.baseurl = tag.attrs['href']
        return self.baseurl

    def complet_url(self, link):
        if link.startswith('/') or link.startswith('.'):
            return urlparse.urljoin(self.baseurl, link)
        elif link.startswith('http') or link.startswith('https'):
            return link
        else:
            return urlparse.urljoin(self.baseurl, link)
            #return False

    def getall(self):
        self.get_tag_a()
        self.get_tag_link()
        self.get_tag_img()
        self.get_tag_script()
        self.get_tag_form()
        self.get_tag_location()
        # links 去重
        for child in self.url_links.keys():
            self.url_links[child] = list(set(self.url_links[child]))
        return self.url_links

    def get_tag_a(self):
        # 处理A链接
        for tag in self.soup.find_all('a'):
            if tag.attrs.has_key('href'):
                link = tag.attrs['href']
                # link = urlparse.urldefrag(tag.attrs['href'])[0] # 处理掉#tag标签信息
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['a'].append(complet_link)
        return self.url_links

    def get_tag_link(self):
        # 处理link链接资源
        for tag in self.soup.find_all('link'):
            if tag.attrs.has_key('href'):
                link = tag.attrs['href']
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['link'].append(complet_link)
        return self.url_links

    def get_tag_img(self):
        for tag in self.soup.find_all('img'):
            if tag.attrs.has_key('src'):
                link = tag.attrs['src']
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['img'].append(complet_link)
        return self.url_links

    def get_tag_script(self):
        for tag in self.soup.find_all('script'):
            if tag.attrs.has_key('src'):
                link = tag.attrs['src']
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['script'].append(complet_link)
        return self.url_links

    def get_tag_location(self):
        for tag in self.soup.find_all('script'):
            text = tag.get_text()
            match = re.search('location(\.href)?\s*?=\s*?[\'"](.*?)[\'"]',text,re.IGNORECASE)
            if match:
                link = match.group(2)
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['location'].append(complet_link)
        return self.url_links

    def get_tag_form(self):
        for tag in self.soup.find_all('form'):
            if tag.attrs.has_key('action'):
                link = tag.attrs['action']
                complet_link = self.complet_url(link.strip())
                if complet_link:
                    self.url_links['form'].append(complet_link)
        return self.url_links

    def get_links_internal(self):
        b = self.getall()
        for a in b:
            for i in b[a]:
                p = urlparse.urlparse(i)
                if  p.netloc == urlparse.urlparse(self.weburl).netloc:
                    self.internal_links.append(i)
                else:
                    continue
        return self.internal_links

    def get_links_external(self):
        for i in self.getall()['a']:
            p = urlparse.urlparse(i)
            if  p.netloc == urlparse.urlparse(self.weburl).netloc:
                continue
            else:
                self.external_links.append(i)
        return self.external_links

def getaction(url):
  import requests
  baseurl = url
  links = []

  resp=None
  try:
    resp = requests.get(url,timeout=20)
    content = resp.content
    baseurl = resp.url

    links = LinksParser(baseurl,content).get_links_internal()
  except:
    pass
  finally:
      if resp is not None:
          resp.close()
  ret=[]
  if len(links)>0:
    ret = filter(fun1, links)

  return ret

def fun1(s):
    if '.action' in s or '.do' in s:
        return s
    else:
        return None
if __name__ == "__main__":
  print getaction('http://www:8089/zhxxgl')