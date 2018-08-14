from plugins import default




from lib.logger import initLog
if __name__ == '__main__':
    logger = initLog('WebDect.log', 3, True)
    a=default.PocController(logger=logger)
    ip='42.120.7.130'
    keywords='elasticsearch'
#     ip=str(sys.argv[1])
#     keywords=str(sys.argv[2])

    a.detect(head='',context='',ip=ip,port='',productname={},keywords=keywords,hackinfo='') 
