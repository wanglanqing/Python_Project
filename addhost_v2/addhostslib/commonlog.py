# coding:utf-8

import logging
import time

class CommonLog(logging.Logger):
    def __init__(self,name):
        logging.Logger.__init__(self,name,logging.DEBUG)
        now = time.strftime('%Y%m%d%H%M%S')
        log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s [%(module)s at line %(lineno)d ,func is %(funcName)s():]  %(message)s ")
        filehandler = logging.FileHandler('addhosts_' + now + '.log')
        filehandler.setFormatter(log_formatter)
        self.addHandler(filehandler)
        return
        # logging.basicConfig(level=logging.DEBUG,
        #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S',
        #                     filename='myapp.log',
        #                     filemode='w')