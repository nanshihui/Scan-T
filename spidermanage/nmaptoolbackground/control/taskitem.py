from spidertool import zmaptool
import random
from datetime import datetime
operator = {'1':'80','2':'8080','3':'443','4':'22','5':'23'}  
def tick():
    num=random.randint(1, 1)

    temp=zmaptool.Zmaptool()
    
    temp.do_scan(port=operator.get(str(num)),num='10',needdetail='1')
    print('Tick! The time is: %s' % datetime.now())
def ticknormal():
    num=random.randint(1, 1)

    temp=zmaptool.Zmaptool()
    
    temp.do_scan(port=operator.get(str(num)),num='100')
    print('Tick! The time is: %s' % datetime.now())