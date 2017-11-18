#coding:utf-8
import os
import platform

class PathManager(object):

    def __init__(self):
        self.dest_host_file_path = ''
        pass

    def get_system_type():
        system_type = platform.system().lower()
        return system_type

    def get_dest_host_file_path():
        system_type = PathManager.get_system_type()
        win_type = 'windows'
        linux_type = 'linux'
        win_sub_path = '\\System32\\drivers\\etc\\hosts'
        linux_host_path = '/etc/hosts'
        win_path_keyword = 'windir'
        if system_type == win_type:
            win_root_path = os.environ[win_path_keyword]
            dest_host_file_path = win_root_path + win_sub_path
            return dest_host_file_path
        elif system_type == linux_type:
            dest_host_file_path = linux_host_path
            return dest_host_file_path

    def get_backup_host_file_path():
        bakup_path = os.getcwd()
        return bakup_path
