import os  
import platform  
import subprocess  
import signal  
import time  
import datetime
class TimeoutError(Exception):  
    pass  
  
def command(cmd, timeout=60):  
    """Run command and return the output 
    cmd - the command to run 
    timeout - max seconds to wait for 
    """  
    is_linux = platform.system() == 'Linux'  
      
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True,shell=True, preexec_fn=os.setsid if is_linux else None)
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


def timeout_command(command, timeout=60):
    start = datetime.datetime.now()
    process = subprocess.Popen(command, bufsize=10000, stdout=subprocess.PIPE, close_fds=True)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            try:
                process.terminate()
            except Exception, e:
                return None
        return None
    out = process.communicate()[0]
    if process.stdin:
        process.stdin.close()
    if process.stdout:
        process.stdout.close()
    if process.stderr:
        process.stderr.close()
    try:
        process.kill()
    except OSError:
        pass
    return out
if __name__ == '__main__':  
    try:  
        result = timeout_command('ping www.site-digger.com', timeout=10)
    except TimeoutError:  
        print 'Run command timeout.'  
    else:  
        print result 