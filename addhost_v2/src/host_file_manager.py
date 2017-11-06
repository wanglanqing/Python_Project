from .argument_definition import ArgumentDefinition
from .text_host_file import TextHostFile
from .windows_host_file import WindowsHostFile
from .linux_host_file import LinuxHostFile
from .excel_host_file import ExcelHostFile
import platform

class HostFileManager(object):

    def __init__(self, argMgr):
        self.argMgr = argMgr
        excel = ArgumentDefinition.get_file_type_argument_excel_choice()
        text  = ArgumentDefinition.get_file_type_argument_text_choice()
        self.source_host_file_workers = {excel: ExcelHostFile,text: TextHostFile}
        self.sys_type = platform.system()
        self.destination_host_file_workers = {'Windows': WindowsHostFile, 'Linux': LinuxHostFile}

    def createSourceHostFileObject(self):
        file_type = self.argMgr.get_file_type_argument_value()
        source_host_file_class = self.source_host_file_workers[file_type]
        return source_host_file_class(self.argMgr)

    def createDestinationHostFileObject(self):
        destination_host_file_class = self.destination_host_file_workers[self.sys_type]
        return destination_host_file_class()
        # if sysstr=='Windows':
        #     return WindowsHostFile()
        #     pass
        # elif sysstr=='Linux':
        #     return LinuxHostFile()
        #     pass