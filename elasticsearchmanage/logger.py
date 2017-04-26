#!/usr/bin/python
# encoding=utf-8


import logging

def initLog(logfile, level=2, verbose=False,name='root'):
	'''
	日志记录函数，日志等级默认为2，即INFO级别的日志
	verbose - 是否屏幕输出，默认False
	'''
	logLevel = logging.INFO
	if level == 0:
		logLevel = logging.NOTSET
	elif level == 1:
		logLevel = logging.DEBUG
	elif level == 2:
		logLevel = logging.INFO
	elif level == 3:
		logLevel = logging.WARNING
	elif level == 4:
		logLevel = logging.ERROR
	elif level == 5:
		logLevel = logging.CRITICAL
	logger = logging.getLogger(name)
	console = logging.FileHandler(logfile)
	formatter = logging.Formatter('[%(asctime)s]%(filename)s-%(process)d-%(thread)d-%(lineno)d-%(levelname)8s-"%(message)s"','%Y-%m-%d %a %H:%M:%S')
	console.setFormatter(formatter)
	logger.addHandler(console)
	logger.setLevel(logLevel)

	if verbose:
		console = logging.StreamHandler()
		console.setLevel(logLevel)	# always debug mode to screen
		formatter = logging.Formatter('%(name)-8s: %(levelname)-8s %(message)s')
		console.setFormatter(formatter)
		logger.addHandler(console)

	return logger

if __name__ == '__main__':
	logger = initLog("logger_test.log", 3, True,'a')
	logger.debug("debug %s", "1")
	logger.info("info %s", "2")
	logger.warning("warning %s", "3")
	logger.error("error %s", "4")
	logger.exception("exception %s", "4")
	logger.critical("critical %s", "5")
	from test import aaaa
	aaaa()

