class Day4Exception(Exception):
    pass

class LowThanZero(Day4Exception):
    err_str = '输入的值小于0'
    def __str__(self):
        return LowThanZero.err_str

class GreatThan12(Day4Exception):
    err_str = '输入的月份大于12'
    def __str__(self):
        return GreatThan12.err_str

class GreatThan31(Day4Exception):
    err_str = '输入的日期大于31'
    def __str__(self):
        return GreatThan31.err_str