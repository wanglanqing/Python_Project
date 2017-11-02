import os
import datetime
import random
class DestinationHostFile(object):

    def __init__(self,dictHosts,argMgr):
        self.dictHosts=dictHosts
        self.argMgr=argMgr
        self.backupType=argMgr.parse_arguments()[argMgr.get_backup_argument_destination_name()]
        self.updateType=argMgr.parse_arguments()[argMgr.get_upadte_argument_destination_name()]
        self.sortType=argMgr.parse_arguments()[argMgr.get_sort_argument_destination_name()]
        pass

    #加载目标文件
    def open(self,filename):
        with open(filename) as f:
            f.readlines()
        print('DestinationHostFile "open()"')
        pass

    def save(self,dictHosts):
        print('Save hosts')
        pass

    def getHostsBakupList(self,dirpath):
        self.dirpath=dirpath
        baklist = []
        retmp = os.listdir(self.dirpath)
        for i in range(len(retmp)):
            if (retmp[i].lower().startswith('hosts')) and (retmp[i].lower().endswith('bak')):
                baklist.append(retmp[i])
        return baklist

    def chdirToSourceFilePath(self):
        print(os.getcwd())
        os.chdir(os.getcwd())

    def chdirToBakupDestinationPath(self):
        print('当前的目录是：{}'.format(os.getcwd()[:-4])+'bakup')
        os.chdir(os.getcwd())

    def buildBackupHostFileName(self,baklist):
        # bakupPath=(os.getcwd())+'bakup'
        # os.chdir(bakupPath)
        timeStamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        multiplicator = 1000
        rNum = str(int(random.random() * multiplicator))
        backupHostFileName='hosts-'+timeStamp+'-'+rNum+'.bak'
        if backupHostFileName in baklist:
            backupHostFileName = 'hosts-' + timeStamp + '-' + (rNum+1) + '.bak'
        print(backupHostFileName)
        return backupHostFileName

    def readOsHostsInfo(self,path):
        self.path = path
        oshosts= open(path+'hosts','r').readlines()
        return oshosts

    def updateHostsByUdateType(self,dictHosts,oshosts):
        self.dictHosts = dictHosts
        print(self.updateType)
        print(self.argMgr.parse_arguments()['update'])
        # for os.hosts in self.dictHosts.values():
        #     if self.argMgr.parseArguments()['update'] == 'update':
        #         print('hostsname存在重复的信息{},更新方式为update，原信息将被覆盖更新'.format())


        pass

    def sortByIP(self):
        pass

    def updateFile(self):
        pass
    def close(self):
        pass

    def __del__(self):
        pass
