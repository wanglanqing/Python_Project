import shutil
import os
from .excel_host_file import ExcelHostFile
from .text_host_file import TextHostFile
from .destination_host_file import DestinationHostFile

class WindowsHostFile(DestinationHostFile):
    # WinsHostsPath = 'C:\Windows\System32\drivers\etc\hosts'
    def __init__(self):
        self.WinsHostsPath ='C:\Windows\System32\drivers\etc\\'
        # self.dictHosts=dictHosts
        # self.argMgr=argMgr
        # self.backupType=argMgr.parseArguments()[argMgr.getBackupArgumentDestinationName()]
        # self.updateType=argMgr.parseArguments()[argMgr.getUpadteArgumentDestinationName()]
        # self.sortType=argMgr.parseArguments()[argMgr.getSortArgumentDestinationName()]
        pass

    def open(self):
        self.hostfile=open(self.WinsHostsPath+'hosts', 'a+')
        pass

    def save(self,dictHosts):
        # os.chdir(self.WinsHostsPath)
        self.dictHosts=dictHosts
        fileinfo=self.hostfile.readlines()
        baklist= super().getHostsBakupList(self.WinsHostsPath)
        backupHostFileName= super().buildBackupHostFileName(baklist)
        super().chdirToBakupDestinationPath()
        #shutil.copyfile("hosts", backupHostFileName)
        # super().updateHostsByUdateType(dictHosts)
        #遍历字典，写入到hosts文件中
        for (host,addr) in dictHosts.items():
            self.hostfile.writelines('\n{} {}'.format(addr,host))

        pass