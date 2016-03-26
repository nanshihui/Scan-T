#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import urlparse
import httplib
import logging
import re
import threading
import Queue
from bs4 import BeautifulSoup
import time
import glob
import socket
import ipaddress
import os
import webbrowser
from lib.interface import InfoDisScannerBase

class InfoDisScanner(InfoDisScannerBase):
    def __init__(self, timeout=600, depth=2):
        self.START_TIME = time.time()
        self.TIME_OUT = timeout
        self.LINKS_LIMIT = 20       # max number of links

        self._init_rules()
    def scanvul(self,url,protocal):
        self.final_severity = 0

        status=self.check_404(url,protocal)           # check the existence of status 404
        if status:
            tempqueue=self._enqueue(url)
            
            self._scan_worker(self,tempqueue,protocal)
        else:
            return None



    def _init_rules(self):
        try:
            self.url_dict = []
            p_severity = re.compile('{severity=(\d)}')
            p_tag = re.compile('{tag="([^"]+)"}')
            p_status = re.compile('{status=(\d{3})}')
            p_content_type = re.compile('{type="([^"]+)"}')
            p_content_type_no = re.compile('{type_no="([^"]+)"}')

            for rule_file in glob.glob('rules/*.txt'):
                infile = open(rule_file, 'r')
                for url in infile:
                    if url.startswith('/'):
                        _ = p_severity.search(url)
                        severity = int(_.group(1)) if _ else 3
                        _ = p_tag.search(url)
                        tag = _.group(1) if _ else ''
                        _ = p_status.search(url)
                        status = int(_.group(1)) if _ else 0
                        _ = p_content_type.search(url)
                        content_type = _.group(1) if _ else ''
                        _ = p_content_type_no.search(url)
                        content_type_no = _.group(1) if _ else ''
                        url = url.split()[0]
                        self.url_dict.append((url, severity, tag, status, content_type, content_type_no))
                        #print (url, severity, tag, status, content_type, content_type_no)
                infile.close()
        except Exception, e:
            logging.error('[Exception in InfoDisScanner._load_dict] %s' % e)

    def _http_request(self, url, timeout=10,protocal='http'):
        conn=None
        try:
            if not url: url = '/'
            conn_fuc = httplib.HTTPSConnection if protocal == 'https' else httplib.HTTPConnection
            conn = conn_fuc(url, timeout=timeout)
            conn.request(method='GET', url=url,
                         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36 BBScan/1.0'}
            )
            resp = conn.getresponse()
            resp_headers = dict(resp.getheaders())
            status = resp.status
            if resp_headers.get('content-type', '').find('text') >= 0 or resp_headers.get('content-type', '').find('html') >= 0 or \
                            int(resp_headers.get('content-length', '0')) <= 1048576:
                html_doc = self._decode_response_text(resp.read())
            else:
                html_doc = ''
            return status, resp_headers, html_doc
        except Exception, e:
            #logging.error('[Exception in InfoDisScanner._http_request] %s' % e)
            return -1, {}, ''
        finally:
            if conn is not None:
                conn.close()
    def _enqueue(self, url):
        url_queue=Queue.Queue()
        for _ in self.url_dict:
            full_url = url.rstrip('/') + _[0]
            url_description = {'prefix': url.rstrip('/'), 'full_url': full_url}
            item = (url_description, _[1], _[2], _[3], _[4], _[5])
            url_queue.put(item)
        return url_queue
            

    @staticmethod
    def _decode_response_text(rtxt, charset=None):
        if charset:
            try:
                return rtxt.decode(charset)
            except:
                pass
        encodings = ['UTF-8', 'GB2312', 'GBK', 'iso-8859-1', 'big5']
        for _ in encodings:
            try:
                return rtxt.decode(_)
            except:
                pass
        try:
            return rtxt.decode('ascii', 'ignore')
        except:
            pass
        raise Exception('Fail to decode response Text')

    def get_status(self, url):
        return self._http_request(url)[0]

    def check_404(self,url,protocal):
        """
        check status 404 existence
        """
        try:
            _status, headers, html_doc = self._http_request(url=url,protocal=protocal)
            if _status == -1:
                print '[ERROR] Fail to connect to %s' % url
                return False

            return True
        except Exception, e:
            return False




    def _get_url(self):
        """
        get url with global lock
        """
        self.lock.acquire()
        if self.url_index_offset < self.len_urls:
            url = self.urls[self.url_index_offset]
        else:
            url = None, None, None
        self.url_index_offset += 1
        self.lock.release()
        return url

    def _update_severity(self, severity):
        if severity > self.final_severity:
            self.final_severity = severity

    def _scan_worker(self,url_queue,protocal):
        while url_queue.qsize() > 0:
            try:
                item = url_queue.get(timeout=1.0)
            except:
                return None
            try:
                url_description, severity, tag, code, content_type, content_type_no = item
                url = url_description['full_url']
                prefix = url_description['prefix']
            except Exception, e:
                logging.error('[InfoDisScanner._scan_worker][1] Exception: %s' % e)
                continue
            if not item or not url:
                break
            try:
                status, headers, html_doc = self._http_request(url=url,protocal=protocal)
                if (status in [200, 301, 302, 303]) and (self.has_404 or status!=self._status):
                    if code and status != code:
                        continue
                    if not tag or html_doc.find(tag) >= 0:
                        if content_type and headers.get('content-type', '').find(content_type) < 0 or \
                            content_type_no and headers.get('content-type', '').find(content_type_no) >=0:
                            continue
                        self.lock.acquire()
                        # print '[+] [Prefix:%s] [%s] %s' % (prefix, status, 'http://' + self.host +  url)
                        if not prefix in self.results:
                            self.results[prefix]= []
                        self.results[prefix].append({'status':status, 'url': '%s://%s%s' % (self.schema, self.host, url)} )
                        self._update_severity(severity)
                        self.lock.release()

                if len(self.results) >= 30:
                    print 'More than 30 vulnerabilities found for [%s], could be false positive.' % self.host
                    return
            except Exception, e:
                logging.error('[InfoDisScanner._scan_worker][2][%s] Exception %s' % (url, e))

  
         
      






if __name__ == '__main__':
        a = InfoDisScanner(url, lock, timeout*60)
        t = threading.Thread(target=self._scan_worker)


        if results:
            for key in results.keys():
                for url in results[key]:
                    print  '[+] [%s] %s' % (url['status'], url['url'])

       

