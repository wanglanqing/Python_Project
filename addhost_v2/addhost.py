from src.argument_manager import ArgumentManager
from src.argument_manager import ArgumentManager
from src.host_file_manager import HostFileManager
from src.argument_exception import ArgumentException

if __name__=='__main__':
    try:
        argMgr = ArgumentManager()
        argMgr.parse_arguments()
        shfMgr = HostFileManager(argMgr)
        srcHostFile = shfMgr.createSourceHostFileObject()
        srcHostFile.open()
        dictHosts = srcHostFile.readHosts()
        destHostFile = shfMgr.createDestinationHostFileObject()
        # destHostFile.open()
        # destHostFile.save(dictHosts)
        # destHostFile.save()
    except ArgumentException as e:
        print(e)
    # except Exception as e:
    #     print(e)


