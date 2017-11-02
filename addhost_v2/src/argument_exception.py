from .argument_definition import ArgumentDefinition

class ArgumentException(Exception):
    pass



class LineNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_line_num_argument_long_name() + " " + ArgumentDefinition.get_line_num_argument_short_name() + " 参数值错误："

class LineNumArgumentLEZeroException(LineNumArgumentException):
    err_str = LineNumArgumentException.prefix + "起始参数不能小于0."
    def __str__(self):
        return LineNumArgumentLEZeroException.err_str

class AddrColNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_addr_col_num_argument_long_name() + " " + ArgumentDefinition.get_addr_col_num_argument_short_name() + " 参数值错误："

class AddrColNumArgumentLEZeroException(AddrColNumArgumentException):
    err_str = AddrColNumArgumentException.prefix + "起始参数不能小于0."
    def __str__(self):
        return AddrColNumArgumentLEZeroException.err_str

class HostColNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_host_name_col_num_argument_long_name() + " " + ArgumentDefinition.get_host_name_col_num_argument_short_name() + " 参数值错误："

class HostColNumArgumentLEZeroException(HostColNumArgumentException):
    err_str = HostColNumArgumentException.prefix + " 起始参数不能小于0."
    def __str__(self):
        return HostColNumArgumentLEZeroException.err_str

class FileNameArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_file_name_argument_long_name() + " " + ArgumentDefinition.get_file_name_argument_short_name() + " 参数值错误："

class FileNameArgumentIsEmptyStringException(ArgumentException):
    err_str = FileNameArgumentException.prefix + '文件名称不能为空的字符串'
    def __str__(self):
        return FileNameArgumentIsEmptyStringException.err_str

class LineNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_line_num_argument_long_name() + " " + ArgumentDefinition.get_line_num_argument_short_name() + " 参数值错误："

class LineNumArgumentOverFlowException(LineNumArgumentException):
    err_str = LineNumArgumentException.prefix + ' 没有指定的行'
    def __str__(self):
        return LineNumArgumentOverFlowException.err_str

class IpAddressColumnNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_addr_col_num_argument_long_name() + " " + ArgumentDefinition.get_addr_col_num_argument_short_name() + " 参数值错误："
class IpAddressColumnNumArgumentOverflowException(IpAddressColumnNumArgumentException):
    err_str = IpAddressColumnNumArgumentException.prefix + ' 没有指定的IP地址列'
    def __str__(self):
        return IpAddressColumnNumArgumentOverflowException.err_str

class HostNameColumnNumArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_host_name_col_num_argument_long_name() + " " + ArgumentDefinition.get_addr_col_num_argument_short_name() + " 参数值错误："

class HostNameColumnNumArgumentOverflowException(HostNameColumnNumArgumentException):
    err_str = HostNameColumnNumArgumentException.prefix + ' 没有指定的HostName列'
    def __str__(self):
        return HostNameColumnNumArgumentOverflowException.err_str

class SheetNameArgumentException(ArgumentException):
    prefix = ArgumentDefinition.get_sheet_name_argument_long_name() + " " + ArgumentDefinition.get_sheet_name_argument_short_name() + " 参数值错误："

class SheetNameArgumentNotFoundException(SheetNameArgumentException):
    err_str = SheetNameArgumentException.prefix + ' 没有指定的sheet'
    def __str__(self):
        return SheetNameArgumentNotFoundException.err_str

class AddrColNumArgumentIsEqualToHostNameColNumArgumentException(ArgumentException):
    err_str = ArgumentDefinition.get_addr_col_num_argument_long_name() + " "\
              + ArgumentDefinition.get_addr_col_num_argument_short_name() + " / "\
              + ArgumentDefinition.get_host_name_col_num_argument_long_name() + " "\
              + ArgumentDefinition.get_host_name_col_num_argument_short_name() + " "\
              + " 两个参数值不能相等"
    def __str__(self):
        return self.err_str
