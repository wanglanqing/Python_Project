# coding:utf-8
from addhostslib.argument_exception import ArgumentException
from addhostslib.argument_manager import ArgumentManager
from addhostslib.destination_exception import DestinationException
from addhostslib.host_file_manager import HostFileManager


if __name__=='__main__':
    try:
        # 构造命令行参数解析管理器，并解析命令行参数
        argMgr = ArgumentManager()
        argMgr.parse_arguments()

        # 创建host文件管理器
        host_file_manager = HostFileManager(argMgr)

        # 创建源host文件处理对象，读取源host文件
        src_host_file_obj = host_file_manager.create_source_host_file_object()
        src_host_file_obj.open()
        src_host_file_obj.read_source_host_file()

        # 创建目标host文件对象，读取目标host文件内容
        desc_host_file_obj = host_file_manager.create_destination_host_file_object()
        desc_host_file_obj.open()
        desc_host_file_obj.read_destination_host_file()
        desc_host_file_obj.merge_hosts(src_host_file_obj.get_ip_hosts_dict(), src_host_file_obj.get_host_ip_dict())
        desc_host_file_obj.save()
    except ArgumentException as e:
        print(e)
    except DestinationException as e:
        print(e)