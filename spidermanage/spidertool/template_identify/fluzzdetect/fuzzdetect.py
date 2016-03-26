#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import urlparse
import httplib
from lib.logger import initLog
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
import callbackfuzz
from __builtin__ import str

class InfoDisScanner(InfoDisScannerBase):
    def __init__(self, timeout=600, depth=2):
        self.START_TIME = time.time()
        self.TIME_OUT = timeout
        self.LINKS_LIMIT = 20       # max number of links
        self.logger=initLog("logger_fuzz.log", 2, True)
        self._init_rules()
    def scanvul(self,ip,protocal,port):
        if len(self.url_dict)==0:
            self._init_rules()
        self.final_severity = 0
        url=ip+':'+str(port)
        status,has404=self.check_404(url=url,protocal=protocal)           # check the existence of status 404
        if status !=-1:
            tempqueue=Queue.Queue()
            self._enqueue(url,tempqueue)
            dataresult=self._scan_worker(url_queue=tempqueue,protocal=protocal,_status=status,has_404=has404,ip=ip,port=port)
            if dataresult is not None:
                callbackfuzz.storedata(ip=ip,port=port,hackinfo=dataresult)
        else:
            pass



    def _init_rules(self):
        try:
            self.url_dict = []
            p_severity = re.compile('{severity=(\d)}')
            p_tag = re.compile('{tag="([^"]+)"}')
            p_status = re.compile('{status=(\d{3})}')
            p_content_type = re.compile('{type="([^"]+)"}')
            p_content_type_no = re.compile('{type_no="([^"]+)"}')
            for rule_file in glob.glob(os.path.split(os.path.realpath(__file__))[0]+'/rules/*.txt'):
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
                        print (url, severity, tag, status, content_type, content_type_no)
                infile.close()
        except Exception, e:
            self.logger.error('[Exception in InfoDisScanner._load_dict] %s' % e)

    def _http_request(self, url, timeout=10,protocal='http',path=None):
        conn=None
        try:
            if not path: path = '/'
            conn_fuc = httplib.HTTPSConnection if protocal == 'https' else httplib.HTTPConnection
            conn = conn_fuc(url, timeout=timeout)
            conn.request(method='GET', url=path,
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
    def _enqueue(self, url,url_queue):
        
        for _ in self.url_dict:
            full_url = url.rstrip('/') + _[0]
            url_description = {'prefix': url.rstrip('/'), 'full_url': full_url}
            item = (url_description, _[1], _[2], _[3], _[4], _[5],_[0])
            url_queue.put(item)

            

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



    def check_404(self,url,protocal):
        """
        check status 404 existence
        """
        _status=0
        has_404=False
        try:
            _status, headers, html_doc = self._http_request(url=url,protocal=protocal,path='/A_NOT_EXISTED_URL_TO_CHECK_404_STATUS_EXISTENCE')
            has_404 = (_status == 404)
            if _status == -1:
                print '[ERROR] Fail to connect to %s' % url
                return -1,has_404

            return _status,has_404
        except Exception, e:
            return _status,has_404



    def _update_severity(self, severity):
        if severity > self.final_severity:
            self.final_severity = severity

    def _scan_worker(self,url_queue,protocal,_status,has_404,ip,port):
        resultarray=[]
        results={}

        while url_queue.qsize() > 0:
            try:
                item = url_queue.get(timeout=1.0)
            except:
                return None
            url=None
            try:
                url_description, severity, tag, code, content_type, content_type_no,path = item

                url = url_description['full_url']
                prefix = url_description['prefix']
            except Exception, e:
                self.logger.error('[InfoDisScanner._scan_worker][1] Exception: %s' % e)
                continue
            if not item or not url:
                break
            try:
                status, headers, html_doc = self._http_request(url=prefix,protocal=protocal,path=path)

                self.logger.info(str(status)+url)
                if (status in [200, 301, 302, 303]) and (has_404 or status!=_status):
                    if code and status != code:
                        continue
                    if not tag or html_doc.find(tag) >= 0:
                        if content_type and headers.get('content-type', '').find(content_type) < 0 or \
                            content_type_no and headers.get('content-type', '').find(content_type_no) >=0:
                            continue

                        # print '[+] [Prefix:%s] [%s] %s' % (prefix, status, 'http://' + self.host +  url)
                        if results.get(prefix,None) is None:
                            results[prefix]= []
                        results[prefix].append({'status':status, 'url': '%s' % (url)} )
                        self._update_severity(severity)


                if len(results) >= 30:
                    print 'More than 30 vulnerabilities found for [%s], could be false positive.' % url
            except Exception, e:
                self.logger.error('[InfoDisScanner._scan_worker][2][%s] Exception %s' % (url, e))

        if len(results) >= 1:
            return results
        

      






if __name__ == '__main__':
        a = InfoDisScanner()
        print a.scanvul(ip='113.105.74.144',port='80',protocal='http')


#         if results:
#             for key in results.keys():
#                 for url in results[key]:
#                     print  '[+] [%s] %s' % (url['status'], url['url'])

       

