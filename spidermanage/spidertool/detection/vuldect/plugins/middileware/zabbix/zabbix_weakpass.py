#coding:utf-8

import requests
from bs4 import BeautifulSoup
import base64,re
from t import T
def _get_static_post_attr(page_content):
    """
    拿到<input type='hidden'>的post参数，并return
    """
    _dict = {}
    soup = BeautifulSoup(page_content, "html.parser")
    for each in soup.find_all('input'):
        if 'value' in each.attrs and 'name' in each.attrs:
            _dict[each['name']] = each['value']
    return _dict
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=10
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        r=None
        s = None
        h1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'

        }

        h2 = {
            'Referer': target_url.strip('\n'),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'

        }

        blacklist = [
            'incorrect',
            '<!-- Login Form -->',

        ]
        try:
            s = requests.session()
            c = s.get(target_url, timeout=10, headers=h1)
            dic = _get_static_post_attr(c.content)
            dic['name'] = 'Admin'
            dic['password'] = 'zabbix'
            # print dic
            r = s.post(target_url + '/index.php', data=dic, headers=h2, timeout=10)
            print r.content
            if 'chkbxRange.init();' in r.content:
                for each in blacklist:
                    if each in r.content:
                        return result
                else:
                    info = ' zabbix Weak password Admin:zabbix'

                    result['result'] = True
                    result['VerifyInfo'] = {}
                    result['VerifyInfo']['type'] = 'zabbix Weak password'
                    result['VerifyInfo']['URL'] = target_url
                    result['VerifyInfo']['result'] = info
                    result['VerifyInfo']['level'] = 'hole'
        except Exception, e:
            print e
        finally:
            if r is not None:
                r.close()
            if s is not None:
                s.close()
            return result











if __name__ == '__main__':
    print P().verify(ip='202.121.168.201',port='9000')