# coding:utf-8
class DestinationException(Exception):
    pass

class ExistsIpAddressException(DestinationException):
    err_str = '错误：在hosts文件中已经存在该ip地址：'
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr

    def __str__(self):
        return ExistsIpAddressException.err_str + self.ipaddr

class DuplicateHostException(DestinationException):
    err_str = "错误：在hosts文件中存在重复的主机名："
    def __init__(self, host_name):
        self.host_name = host_name

    def __str__(self):
        return DuplicateHostException.err_str + self.host_name
