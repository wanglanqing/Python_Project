from .argument_definition import ArgumentDefinition
from .text_host_file import TextHostFile
from .windows_host_file import WindowsHostFile
from .linux_host_file import LinuxHostFile
from .excel_host_file import ExcelHostFile
import platform

class HostFileManager(object):

    def __init__(self, argMgr):
        self.argMgr = argMgr
        self.source_host_file_workers = {}
        excel = ArgumentDefinition.get_file_type_argument_excel_choice()
        self.regist_source_host_file_worker(excel, ExcelHostFile)
        text  = ArgumentDefinition.get_file_type_argument_text_choice()
        self.regist_source_host_file_worker(text, TextHostFile)

    def createSourceHostFileObject(self):
        file_type = self.argMgr.get_file_type_argument_value()
        worker = self.source_host_file_workers[file_type]
        return worker(self.argMgr)

    def createDestinationHostFileObject(self):
        sysstr = platform.system()
        if sysstr=='Windows':
            return WindowsHostFile()
            pass
        elif sysstr=='Linux':
            return LinuxHostFile()
            pass

    def regist_source_host_file_worker(self, file_type, worker):
        self.source_host_file_workers[file_type] = worker