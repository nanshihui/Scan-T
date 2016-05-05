#!/usr/bin/python
#coding:utf-8
import logging
logger=None

def getObject():
    global logger
    if logger is None:
# 创建一个logger
        logger = logging.getLogger('debug')
        logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
        fh = logging.FileHandler('logs/debugspidertool.log')
        fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
# 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


# 记录一条日志
# 
# logger.debug("foobar")    # 不输出   
# logger.info("foobar")        # 输出  
# logger.warning("foobar")  # 输出  
# logger.error("foobar")      # 输出  
# logger.critical("foobar")    # 输出  

