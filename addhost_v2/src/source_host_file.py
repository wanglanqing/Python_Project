'''
create hostfile object
'''
from .argument_manager import ArgumentManager
import os
class SourceHostFile(object):

    # 创建文件对象
    def __init__(self, argMgr):
        self.argMgr = argMgr
        self.lines = []
        self.is_open = False
        print('SourceHostFile construtor')
        pass

    def open(self):
        print('SourceHostFile "open()"')
        #在派生类中设置isOpen标志
        #isOpen = True
        pass

    def readHosts(self):
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

