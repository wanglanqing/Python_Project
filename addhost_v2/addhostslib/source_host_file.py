#coding:utf-8
from .commonlog import CommonLog
import logging

class SourceHostFile(object):

    # 创建文件对象
    def __init__(self, argMgr):
        logging.setLoggerClass(CommonLog)
        self.logger = logging.getLogger(__name__)
        self.argMgr = argMgr
        self.lines = []
        self.ip_hosts_dict = {}
        self.host_ip_dict = {}
        self.is_open = False
        self.logger.info('SourceHostFile construtor')
        pass

    def stript(self, str_list, chars=None):
        for i in range(len(str_list)):
            str_list[i] = str_list[i].strip(chars)
        return str_list

    def get_ip_hosts_dict(self):
        return self.ip_hosts_dict

    def get_host_ip_dict(self):
        return self.host_ip_dict

    def open(self):
        self.logger.info('SourceHostFile "open()"')
        #在派生类中设置isOpen标志
        #isOpen = True
        pass

    def read_source_host_file(self):
        self.logger.info('SourceHostFile "read()"')
        return {}
        pass

    def close(self):
        self.logger.info('SourceHostFile "close()"')
        pass

    def __del__(self):
        self.logger.info('SourceHostFile: __del__')
        if self.is_open :
            self.close()
            self.is_open = False
        self.logger.info(self.fileName,'is closed')
        pass

