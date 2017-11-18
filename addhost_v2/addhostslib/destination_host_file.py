# coding:utf-8
import datetime
import random
import re
import os
import shutil
from .path_manager import PathManager
from .argument_definition import ArgumentDefinition
from .destination_exception import *
from .commonlog import CommonLog
import logging


class WindowsHostFile(object):
    def __init__(self, argMgr):
        logging.setLoggerClass(CommonLog)
        self.logger = logging.getLogger(__name__)
        self.argMgr=argMgr
        self.dest_host_file_stream = None
        self.dest_host_file_lines = []
        self.ipaddr_line_content_dict = {}
        self.host_ip_dict = {}
        self.bakup_file_name = self.argMgr.get_backup_argument_value()

    def open(self):
        self.dest_host_file_stream = open(PathManager.get_dest_host_file_path(), "r+")
        pass

    def parse_lines_to_dict(self):
        line_index = -1
        for line in self.dest_host_file_lines:
            line_index += 1
            if line.startswith("#"):
                continue
            if line == "":
                continue
            ipaddr = ""
            comment = ""
            hosts = []
            templist = line.split("#", 2)
            if len(templist) == 2:
                comment = templist[1]
            templist = re.split("\s+", templist[0].strip())
            ipaddr = templist[0]
            hosts = templist[1:]
            self.ipaddr_line_content_dict[ipaddr]=[line_index, ipaddr, set(hosts), comment]
            for host in hosts:
                if host in self.host_ip_dict:
                    self.logger(DuplicateHostException(host))
                    raise DuplicateHostException(host)
                self.host_ip_dict[host]=ipaddr

    def read_destination_host_file(self):
        self.dest_host_file_lines = self.dest_host_file_stream.readlines()
        for i in range(0, len(self.dest_host_file_lines)):
            self.dest_host_file_lines[i] = self.dest_host_file_lines[i].strip()
        self.parse_lines_to_dict()

    def merge_hosts(self, src_ip_hosts_dict, src_host_ip_dict):
        operation = self.argMgr.get_upadte_argument_value()
        for ipaddr in src_ip_hosts_dict:
            if ipaddr in self.ipaddr_line_content_dict:
                src_host_set = src_ip_hosts_dict[ipaddr]
                if operation == ArgumentDefinition.get_update_argument_replace_choice():
                    self.ipaddr_line_content_dict[ipaddr][2] = src_host_set
                    for host in src_host_set:
                        if host in self.host_ip_dict:
                            if ipaddr != self.host_ip_dict[host]:
                                self.ipaddr_line_content_dict[self.host_ip_dict[host]][2].remove(host)
                    continue
                elif operation == ArgumentDefinition.get_update_argument_append_choice():
                    self.ipaddr_line_content_dict[ipaddr][2].update(src_host_set)
                    for host in src_host_set:
                        if host in self.host_ip_dict:
                            if ipaddr != self.host_ip_dict[host]:
                                self.ipaddr_line_content_dict[self.host_ip_dict[host]][2].remove(host)
                    continue
                elif operation == ArgumentDefinition.get_update_argument_ignore_choice():
                    continue
                elif operation == ArgumentDefinition.get_update_argument_terminate_choice():
                    self.logger(ExistsIpAddressException(ipaddr))
                    raise ExistsIpAddressException(ipaddr)
            else:
                src_host_set = src_ip_hosts_dict[ipaddr]
                new_idx = len(self.dest_host_file_lines)
                self.ipaddr_line_content_dict[ipaddr] = [new_idx, ipaddr, src_host_set, ""]
                for host in src_host_set:
                    if host in self.host_ip_dict:
                        if ipaddr != self.host_ip_dict[host]:
                            other_ipaddr_host_set = self.ipaddr_line_content_dict[self.host_ip_dict[host]][2]
                            other_ipaddr_host_set.remove(host)

    def update_line(self, line_content):
        idx = line_content[0]
        ipaddr = line_content[1]
        host_set = line_content[2]
        comment = line_content[3]
        if comment != "":
            comment = "\t#" + comment
        hosts_str = ""
        for host in host_set:
            if hosts_str == "":
                hosts_str = host
                continue
            hosts_str += "\t" + host
        hosts_str = hosts_str.strip()
        if hosts_str == "":
            self.dest_host_file_lines[idx] = ""
            return

        if idx < len(self.dest_host_file_lines):
            self.dest_host_file_lines[idx] = "%s\t%s%s" % (ipaddr, hosts_str, comment)
        else:
            self.dest_host_file_lines.append("%s\t%s%s" % (ipaddr, hosts_str, comment))

    def save(self):
        # 依据self.ipaddr_line_content_dict的内容，更新self.dest_host_file_lines的内容
        self.bakup_destination_host_file()
        for ipaddr in self.ipaddr_line_content_dict:
            self.update_line(self.ipaddr_line_content_dict[ipaddr])

        # 将文件指针移动到文件头，写入更新后的hosts文件
        self.dest_host_file_stream.seek(0)
        for line in self.dest_host_file_lines:
            self.dest_host_file_stream.write(line + "\n")
        self.dest_host_file_stream.flush()
        self.dest_host_file_stream.truncate()

    def bakup_destination_host_file(self):
        bakup_file_list = os.listdir(PathManager.get_backup_host_file_path())
        if self.bakup_file_name == None:
            time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            multiplicator = 1000
            rand_num = int(random.random() * multiplicator)
            backup_host_file_name = 'hosts-%s-%03d.bak' %(time_stamp, rand_num)
            while (backup_host_file_name in bakup_file_list):
                backup_host_file_name =  'hosts-%s-%03d.bak' %(time_stamp, rand_num+1)
            shutil.copyfile(PathManager.get_dest_host_file_path(), PathManager.get_backup_host_file_path() + backup_host_file_name)
        else:
            try:
                shutil.copyfile(PathManager.get_dest_host_file_path() , self.bakup_file_name)
            except Exception as e:
                self.logger('指定的备份路径有误：',e)