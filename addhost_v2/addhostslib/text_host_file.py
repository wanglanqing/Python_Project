#coding:utf-8
from .source_host_file import SourceHostFile
from .argument_exception import *
from .commonlog import CommonLog
import logging

class TextHostFile(SourceHostFile):
    def __init__(self, argMgr):
        logging.setLoggerClass(CommonLog)
        self.logger = logging.getLogger(__name__)
        super(TextHostFile, self).__init__(argMgr)
        self.logger.info('TextHostFile construtor')
        pass

    def open(self):
        self.logger.info('TextHostFile "open()"')
        self.text_file_stream = open(self.argMgr.get_file_name_argument_value())
        self.is_open = True

    def read_source_host_file(self):
        # 获得命令行参数
        begin = self.argMgr.get_line_num_argument_value() - 1
        delimiter = self.argMgr.get_delimiter_argument_value()
        addr_col_num = self.argMgr.get_addr_col_num_argument_value() - 1
        host_name_col_num = self.argMgr.get_host_name_col_num_argument_value() - 1

        # 读取hosts文件到lines列表
        lines = self.text_file_stream.readlines()
        if len(lines) <= begin:
            self.logger.error(LineNumArgumentOverFlowException())
            raise LineNumArgumentOverFlowException()

        if addr_col_num == host_name_col_num:
            self.logger.error(AddrColNumArgumentIsEqualToHostNameColNumArgumentException())
            raise AddrColNumArgumentIsEqualToHostNameColNumArgumentException()

        # 从line_num开始读取数据行，并且构造self.ip_host_dict字典表
        for idx in range(begin, len(lines)):
            line = lines[idx]
            cols = self.stript(line.split(delimiter))
            if len(cols) <= addr_col_num:
                self.logger.error(IpAddressColumnNumArgumentOverflowException())
                raise IpAddressColumnNumArgumentOverflowException()
            if len(cols) <= host_name_col_num:
                self.logger.error(HostNameColumnNumArgumentOverflowException())
                raise HostNameColumnNumArgumentOverflowException()
            ip_addr = cols[addr_col_num]
            host = cols[host_name_col_num]
            host_set = set()
            if ip_addr in self.ip_hosts_dict:
                host_set = self.ip_hosts_dict[ip_addr]
            else:
                self.ip_hosts_dict[ip_addr] = host_set
            host_set.add(host)
            self.host_ip_dict[host] = ip_addr

    def __str__(self):
        return self.ip_host_dict

    def close(self):
     self.close(self.text_file_stream)
     self.logger.info('TextHostFile "close()"')
     pass

    def __del__(self):
     self.logger.info('TextHostFile.__del__')
     pass