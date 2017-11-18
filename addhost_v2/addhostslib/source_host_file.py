#coding:utf-8

class SourceHostFile(object):

    # 创建文件对象
    def __init__(self, argMgr):
        self.argMgr = argMgr
        self.lines = []
        self.ip_hosts_dict = {}
        self.host_ip_dict = {}
        self.is_open = False
        print('SourceHostFile construtor')
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
        print('SourceHostFile "open()"')
        #在派生类中设置isOpen标志
        #isOpen = True
        pass

    def read_source_host_file(self):
        print('SourceHostFile "read()"')
        return {}
        pass

    def close(self):
        print('SourceHostFile "close()"')
        pass

    def __del__(self):
        print('SourceHostFile: __del__')
        if self.is_open :
            self.close()
            self.is_open = False
        print(self.fileName,'is closed')
        pass

