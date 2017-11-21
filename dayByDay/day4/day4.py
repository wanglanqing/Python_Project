'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
from day4.day4exception import *

class GetDays(object):
    def __init__(self):
        self.date_dict = {}

    def get_date(self,year,month,day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        # self.target_year = int(input('请输入指定的年：'))
        if self.year <= 0:
            raise LowThanZero()
        self.date_dict['year'] = self.year

        # self.target_month = int(input('请输入指定的月：'))
        if self.month <=0 :
            raise LowThanZero()
        elif self.month > 12:
            raise GreatThan12()
        self.date_dict['month'] = self.month

        # self.target_day = int(input('请输入日：'))
        if self.day <= 0:
            raise LowThanZero()
        elif self.day >31:
            raise GreatThan31()
        self.date_dict['day'] = self.day
        return self.date_dict

    def is_leap_year(self):
        if (self.date_dict['year'] % 4 ==0) and (self.date_dict['year'] % 100 !=0):
            return True

    def get_days(self):
        dayue = [1, 3, 5, 7, 8, 10, 12]
        xiaoyue = [4, 6, 9, 11]
        days = 0
        for i in range(1, self.date_dict['month']):
            if i in dayue:
                tmpdays = 31
            elif i in xiaoyue:
                tmpdays = 30
            elif self.is_leap_year():
                tmpdays = 29
            else:
                tmpdays = 28
            days += tmpdays
        days = days + self.date_dict['day']
        print(days)
        return days


if __name__ == '__main__':
    try:
        gd = GetDays()
        gd.get_date(2012.7,12,31)
        gd.get_days()
    except Exception as e:
        print(e)