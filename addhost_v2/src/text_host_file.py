from .source_host_file import SourceHostFile
from .argument_exception import *
class TextHostFile(SourceHostFile):
    def __init__(self, argMgr):
         super(TextHostFile, self).__init__(argMgr)
         self.ip_host_dict = {}
         print('TextHostFile construtor')
         pass

    def open(self):
        print('TextHostFile "open()"')
        self.text_file = open(self.argMgr.get_file_name_argument_value())
        self.is_open = True

    def readHosts(self):
        # 获得命令行参数
        line_num = self.argMgr.get_line_num_argument_value()
        delimiter = self.argMgr.get_delimiter_argument_value()
        addr_col_num = self.argMgr.get_addr_col_num_argument_value()
        host_name_col_num = self.argMgr.get_host_name_col_num_argument_value()

        # 读取hosts文件到lines列表
        lines = self.text_file.readlines()
        if len(lines) < line_num:
            raise LineNumArgumentOverFlowException()

        if addr_col_num == host_name_col_num:
            raise AddrColNumArgumentIsEqualToHostNameColNumArgumentException()

        # 从line_num开始读取数据行，并且构造self.ip_host_dict字典表
        begin = line_num - 1
        for idx in range(begin, len(lines)):
            line = lines[idx].strip()
            cols = line.split(delimiter)
            if len(cols) < addr_col_num:
                raise IpAddressColumnNumArgumentOverflowException()
            if len(cols) < host_name_col_num:
                raise HostNameColumnNumArgumentOverflowException()
            self.ip_host_dict[cols[addr_col_num - 1].strip()]=[cols[host_name_col_num - 1].strip()]
        return self.ip_host_dict

    def __str__(self):
        return self.ip_host_dict

    def close(self):
     self.close(self.text_file)
     print('TextHostFile "close()"')
     pass

    def __del__(self):
     print('TextHostFile.__del__')
     # SourceHostFile.__del__(self)
     pass