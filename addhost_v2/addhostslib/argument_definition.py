# coding:utf-8
import argparse

class ArgumentDefinition(object):
    file_name = "filename"
    file_type = "filetype"
    delimiter = "delimiter"
    line_num = "linenum"
    addr_col = "addrcol"
    host_name_col = 'hostnamecol'
    backup = "backup"
    operate = "operate"
    sort = "sort"
    sheet_name = 'sheetname'
    argument_name_dictionary = {
        file_name: {'shortname': '-f', 'longname': '--file-name', 'dest': file_name,
                     'help': "指定用于读入ip和主机名的源文件，必须指定该参数"},
        file_type: {'shortname': '-t', 'longname': '--file-type', 'dest': file_type, 'choices': ['text', 'excel'],
                     'help': "用于指定源文件的类型，有效值为：excel、text，默认为“text”，当参数值为“text”时，可以指定文件中字段的分隔符号，参考“-d”参数说明"},
        delimiter: {'shortname': '-d', 'longname': '--delimiter', 'dest': delimiter,
                      'help': "当“-t”参数值为“text”时，由该参数指定源文件中字段的分隔符号，默认为“,”，当-t参数值不是“text”时，忽略该参数"},
        line_num: {'shortname': '-n', 'longname': '--line-number', 'dest': line_num,
                    'help': "指定从源文件读取数据的起始行号，行号从1开始"},
        addr_col: {'shortname': '-a', 'longname': '--addr-column', 'dest': addr_col,
                    'help': "指定ip地址在源文件中的字段号，字段号从1开始,必须指定该参数"},
        host_name_col: {'shortname': '-h', 'longname': '--host-name-column', 'dest': host_name_col,
                        'help': "指定主机名在源文件中的字段号，字段号从1开始,必须指定该参数"},
        backup: {'shortname': '-b', 'longname': '--backup-host-file', 'dest': backup,
                   'help': "指定在添加主机配置数据前备份hosts文件的备份文件名，默认在当前目录下备份hosts为hosts-<YYYYMMDDHHMISS>-<###>.bak文件，如果该文件已经存在，随机数加一再继续保存，直到备份文件不存在可以保存为止"},
        operate: {'shortname': '-o', 'longname': '--operate-host-file', 'dest': operate, 'choices': ['replace', 'append',  'ignore', 'terminate'],
                   'help': "当源文件的主机名已经在hosts文件中时，该参数用于指定命令的处理方式，update: 更新，ignore: 忽略，terminate: 不更新并且终止命令的继续执行。默认值为update"},
        sort: {'shortname': '-s', 'longname': '--sort-byIP', 'dest': sort, 'choices': ['none', 'asc', 'desc'],
                 'help': "指定在添加主机配置数据时，以IP地址排序的方式，asc: 升序，desc: 降序，none: 不排序，保持原有顺序。默认为“none”"},
        sheet_name: {'shortname': '-e', 'longname': '--sheet-name', 'dest': sheet_name,
               'help': "当“-t”参数值为“excel”时，由该参数指定源文件中要使用的sheet，当-t参数值不是“excel”时，忽略该参数"}
    }

    # file_name
    def get_file_name_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_name]['shortname']

    def get_file_name_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_name]['longname']

    def get_file_name_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_name]['dest']

    def get_file_name_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_name]['help']

    # === file_type ===
    def get_file_type_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_type]['shortname']
    def get_file_type_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_type]['longname']
    def get_file_type_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_type]['dest']
    def get_file_type_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_type]['help']
    def get_file_type_argument_choices():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.file_type]['choices']
    def get_file_type_argument_text_choice():
        return ArgumentDefinition.get_file_type_argument_choices()[0]
    def get_file_type_argument_excel_choice():
        return ArgumentDefinition.get_file_type_argument_choices()[1]

    # === delimiter ===
    def get_delimiter_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.delimiter]['shortname']
    def get_delimiter_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.delimiter]['longname']
    def get_delimiter_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.delimiter]['dest']
    def get_delimiter_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.delimiter]['help']

    def get_line_num_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.line_num]['shortname']
    def get_line_num_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.line_num]['longname']
    def get_line_num_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.line_num]['dest']
    def get_line_num_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.line_num]['help']

    def get_addr_col_num_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.addr_col]['shortname']
    def get_addr_col_num_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.addr_col]['longname']
    def get_addr_col_num_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.addr_col]['dest']
    def get_addr_col_num_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.addr_col]['help']

    def get_host_name_col_num_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.host_name_col]['shortname']
    def get_host_name_col_num_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.host_name_col]['longname']
    def get_host_name_col_num_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.host_name_col]['dest']
    def get_host_name_col_num_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.host_name_col]['help']

    def get_backup_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.backup]['shortname']
    def get_backup_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.backup]['longname']
    def get_backup_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.backup]['dest']
    def get_backup_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.backup]['help']

    def get_update_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.operate]['shortname']
    def get_update_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.operate]['longname']
    def get_update_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.operate]['dest']
    def get_update_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.operate]['help']
    def get_update_argument_choices():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.operate]['choices']
    def get_update_argument_replace_choice(): #['replace', 'append',  'ignore', 'terminate']
        return ArgumentDefinition.get_update_argument_choices()[0]
    def get_update_argument_append_choice():
        return ArgumentDefinition.get_update_argument_choices()[1]
    def get_update_argument_ignore_choice():
        return ArgumentDefinition.get_update_argument_choices()[2]
    def get_update_argument_terminate_choice():
        return ArgumentDefinition.get_update_argument_choices()[3]

    def get_sort_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sort]['shortname']
    def get_sort_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sort]['longname']
    def get_sort_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sort]['dest']
    def get_sort_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sort]['help']
    def get_sort_argument_choices():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sort]['choices']

    def get_sheet_name_argument_short_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sheet_name]['shortname']
    def get_sheet_name_argument_long_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sheet_name]['longname']
    def get_sheet_name_argument_destination_name():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sheet_name]['dest']
    def get_sheet_name_argument_help_info():
        return ArgumentDefinition.argument_name_dictionary[ArgumentDefinition.sheet_name]['help']

if __name__ == '__main__':
    print(ArgumentDefinition.get_file_name_argument_short_name())
