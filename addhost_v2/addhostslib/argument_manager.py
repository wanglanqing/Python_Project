#coding:utf-8
import argparse
from .argument_exception import *
from .commonlog import CommonLog
import logging

class ArgumentManager(object):
    def __init__(self):
        logging.setLoggerClass(CommonLog)
        self.logger = logging.getLogger(__name__)
        self.create_argument_parser()
        self.add_file_name_argument()
        self.add_file_type_argument()
        self.add_delimiter_argument()
        self.add_start_line_number_argument()
        self.add_ip_address_column_number_argument()
        self.add_host_name_column_number_argument()
        self.add_backup_host_file_name_argument()
        self.add_update_type_argument()
        self.add_sort_type_argument()
        self.add_sheet_name_argument()


    def create_argument_parser(self):
        self.parser = argparse.ArgumentParser(
            conflict_handler='resolve',
            epilog="如何使用命令参数： \
	        addhostslib -f <filename> ,\
	        addhostslib -f <filename> [-t excel] [-n <linenum>] [-a ipaddrcolumn] [-h hostcolumn] [-b <bakeupname>] [-u true|false] [-s {asc|desc|none}] , \
	        addhostslib -f <filename> [-t text [-d <delimiter>] [-n <linenum>] [-a ipaddrcolumn] [-h hostcolumn] [-b <bakeupname>] [-u {update|ignore|terminate}] [-s {asc|desc|none}] , \
	        addhostslib -v|? "
        )

#添加命令行参数
    def add_file_name_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_file_name_argument_short_name(),
                                 ArgumentDefinition.get_file_name_argument_long_name(),
                                 help=ArgumentDefinition.get_file_name_argument_help_info(),
                                 required=True,
                                 default=None,
                                 # nargs=1,
                                 metavar='<filename>',
                                 dest=ArgumentDefinition.get_file_name_argument_destination_name()
                                 )

    def add_file_type_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_file_type_argument_short_name(),
                                 ArgumentDefinition.get_file_type_argument_long_name(),
                                 help=ArgumentDefinition.get_file_type_argument_help_info(),
                                 choices=ArgumentDefinition.get_file_type_argument_choices(),
                                 default=ArgumentDefinition.get_file_type_argument_choices()[0],
                                 dest=ArgumentDefinition.get_file_type_argument_destination_name()
                                 )

    def add_delimiter_argument(self):
        # 当-t为text时，该参数可使用；当-t为excel时，忽略该参数
        self.parser.add_argument(ArgumentDefinition.get_delimiter_argument_short_name(),
                                 ArgumentDefinition.get_delimiter_argument_long_name(),
                                 help=ArgumentDefinition.get_delimiter_argument_help_info(),
                                 dest=ArgumentDefinition.get_delimiter_argument_destination_name(),
                                 default=','
                                 )

    def add_start_line_number_argument(self):
        # 从源文件读取数据的起始行号
        self.parser.add_argument(ArgumentDefinition.get_line_num_argument_short_name(),
                                 ArgumentDefinition.get_line_num_argument_long_name(),
                                 help=ArgumentDefinition.get_line_num_argument_help_info(),
                                 dest=ArgumentDefinition.get_line_num_argument_destination_name(),
                                 type=int
                                 )

    def add_ip_address_column_number_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_addr_col_num_argument_short_name(),
                                 ArgumentDefinition.get_addr_col_num_argument_long_name(),
                                 help=ArgumentDefinition.get_addr_col_num_argument_help_info(),
                                 dest=ArgumentDefinition.get_addr_col_num_argument_destination_name(),
                                 type=int,
                                 required=True
                                 )

    def add_host_name_column_number_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_host_name_col_num_argument_short_name(),
                                 ArgumentDefinition.get_host_name_col_num_argument_long_name(),
                                 help=ArgumentDefinition.get_host_name_col_num_argument_help_info(),
                                 dest=ArgumentDefinition.get_host_name_col_num_argument_destination_name(),
                                 type=int,
                                 required=True
                                 )

    def add_backup_host_file_name_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_backup_argument_short_name(),
                                 ArgumentDefinition.get_backup_argument_long_name(),
                                 help=ArgumentDefinition.get_backup_argument_help_info(),
                                 dest=ArgumentDefinition.get_backup_argument_destination_name()
                                 )

    def add_update_type_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_update_argument_short_name(),
                                 ArgumentDefinition.get_update_argument_long_name(),
                                 help=ArgumentDefinition.get_update_argument_help_info(),
                                 choices=ArgumentDefinition.get_update_argument_choices(),
                                 default=ArgumentDefinition.get_update_argument_choices()[0],
                                 dest=ArgumentDefinition.get_update_argument_destination_name(),
                                 )

    def add_sort_type_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_sort_argument_short_name(),
                                 ArgumentDefinition.get_sort_argument_long_name(),
                                 help=ArgumentDefinition.get_sort_argument_help_info(),
                                 dest=ArgumentDefinition.get_sort_argument_destination_name(),
                                 nargs='?',
                                 choices=ArgumentDefinition.get_sort_argument_choices(),
                                 default = ArgumentDefinition.get_sort_argument_choices()[0],
                                 )

    def add_sheet_name_argument(self):
        self.parser.add_argument(ArgumentDefinition.get_sheet_name_argument_short_name(),
                                 ArgumentDefinition.get_sheet_name_argument_long_name(),
                                 dest = ArgumentDefinition.get_sheet_name_argument_destination_name(),
                                 help = ArgumentDefinition.get_sheet_name_argument_help_info(),
                                 type = str,
                                 nargs = '?'
        )
    # =======================================================
    # 获取参数值系列方法：get_******_argument_value()
    # -------------------------------------------------------
    def get_file_name_argument_value(self):
        return self.file_name_argument_value

    def get_file_type_argument_value(self):
        return self.file_type_argument_value

    def get_line_num_argument_value(self):
        return self.line_num_argument_value

    def get_delimiter_argument_value(self):
        return self.delimiter_argument_value

    def get_addr_col_num_argument_value(self):
        return self.addr_col_num_argument_value

    def get_host_name_col_num_argument_value(self):
        return self.host_name_col_num_argument_value

    def get_upadte_argument_value(self):
        return self.update_argument_value

    def get_sort_argument_value(self):
        return self.sort_argument_value

    def get_backup_argument_value(self):
        return self.backup_argument_value

    def get_sheet_name_argument_value(self):
        return self.sheet_name_argument_value
    # -------------------------------------------------------

    def parse_arguments(self):
        self.args = vars(self.parser.parse_args())
        self.logger.info('参数信息为：')
        self.logger.info(self.args)
        self.file_name_argument_value = self.args[ArgumentDefinition.get_file_name_argument_destination_name()]
        if self.file_name_argument_value == "" or self.file_name_argument_value == None:
            self.logger.error(FileNameArgumentIsEmptyStringException())
            raise FileNameArgumentIsEmptyStringException()

        self.file_type_argument_value = self.args[ArgumentDefinition.get_file_type_argument_destination_name()]

        self.line_num_argument_value = self.args[ArgumentDefinition.get_line_num_argument_destination_name()]
        if self.line_num_argument_value <= 0:
            self.logger.error(LineNumArgumentLEZeroException())
            raise LineNumArgumentLEZeroException()

        self.delimiter_argument_value = self.args[ArgumentDefinition.get_delimiter_argument_destination_name()]

        self.addr_col_num_argument_value = self.args[ArgumentDefinition.get_addr_col_num_argument_destination_name()]
        if self.addr_col_num_argument_value <=0:
            self.logger.error(AddrColNumArgumentLEZeroException())
            raise AddrColNumArgumentLEZeroException()

        self.host_name_col_num_argument_value = self.args[ArgumentDefinition.get_host_name_col_num_argument_destination_name()]
        if self.host_name_col_num_argument_value <= 0 :
            self.logger.error(HostColNumArgumentLEZeroException())
            raise  HostColNumArgumentLEZeroException()

        self.update_argument_value = self.args[ArgumentDefinition.get_update_argument_destination_name()]

        self.sort_argument_value = self.args[ArgumentDefinition.get_sort_argument_destination_name()]

        self.backup_argument_value = self.args[ArgumentDefinition.get_backup_argument_destination_name()]

        self.sheet_name_argument_value = self.args[ArgumentDefinition.get_sheet_name_argument_destination_name()]

    def __str__(self):
        mystr  = ArgumentDefinition.get_file_name_argument_destination_name() + " = " + self.file_name_argument_value + "\n"
        mystr += ArgumentDefinition.get_file_type_argument_destination_name() + " = " + self.file_type_argument_value  + "\n"
        mystr += ArgumentDefinition.get_line_num_argument_destination_name() + " = " + str(self.line_num_argument_value) + "\n"
        mystr += ArgumentDefinition.get_delimiter_argument_destination_name() + " = " + self.delimiter_argument_value + "\n"
        mystr += ArgumentDefinition.get_addr_col_num_argument_destination_name() + " = " + str(self.addr_col_num_argument_value) + "\n"
        mystr += ArgumentDefinition.get_host_name_col_num_argument_destination_name() + " = " + str(self.host_name_col_num_argument_value) + "\n"
        mystr += ArgumentDefinition.get_update_argument_destination_name() + " = " + self.update_argument_value + "\n"
        mystr += ArgumentDefinition.get_sort_argument_destination_name() + " = " + self.sort_argument_value + "\n"
        mystr += ArgumentDefinition.get_backup_argument_destination_name() + " = " + str(self.backup_argument_value) + "\n"
        mystr += ArgumentDefinition.get_sheet_name_argument_destination_name() + " = " + self.sheet_name_argument_value
        return mystr