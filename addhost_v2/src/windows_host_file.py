import shutil
import os
import re
from .excel_host_file import ExcelHostFile
from .text_host_file import TextHostFile
from .destination_host_file import DestinationHostFile

class WindowsHostFile(DestinationHostFile):
    # HostsPath = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    HostsPath = './file/hosts.txt'
    def __init__(self):
        self.destination_file = None
        self.destination_hosts = {}

        pass

    def open(self):
        self.destination_file = open(self.HostsPath)
        pass

    def save(self,dictHosts):
        # os.chdir(self.WinsHostsPath)
        self.dictHosts=dictHosts
        destination_hosts_file = super().read_destination_hosts(self.HostsPath)
        print(destination_hosts_file)
        # baklist= super().getHostsBakupList(self.WinsHostsPath)
        # backupHostFileName= super().buildBackupHostFileName(baklist)
        # super().chdirToBakupDestinationPath()
        # #shutil.copyfile("hosts", backupHostFileName)
        # # super().updateHostsByUdateType(dictHosts)
        # #遍历字典，写入到hosts文件中
        # for (host,addr) in dictHosts.items():
        #     self.hostfile.writelines('\n{} {}'.format(addr,host))

        pass

    def read_destination_hosts(self):
        self.destination_hosts = self.destination_file.readlines()
        for i in range(0, len(self.destination_hosts)):
            self.destination_hosts[i] = self.destination_hosts[i].strip()
        return self.destination_hosts

    def parse_lines_to_dict(self):
        line_index = -1
        ipaddr_dict = {}
        host_dict = {}
        for line in self.destination_hosts:
            line_index += 1
            if line.startswith("#"):
                continue
            if line == "":
                continue
            ipaddr = ""
            comment = ""
            hsots = []
            templist = line.split("#", 2)
            if len(templist) == 2:
                comment = templist[1]
            templist = re.split("\s+", templist[0])
            ipaddr = templist[0]
            hosts = templist[1:]
            ipaddr_dict[ipaddr]=[line_index, ipaddr, hosts, comment]
            for host in hosts:
                if host in hosts:
                    raise
                host_dict[host]=ipaddr


            print(line_index,line.split(' '))
            ipaddr_dict[line.split(' ')[0]]= line.split(' ')[1:]

        print(ipaddr_dict)
        myIP = '123.57.56.123'
        print(myIP in ipaddr_dict.keys())