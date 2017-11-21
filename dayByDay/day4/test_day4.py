from day4.day4 import *
import pytest
from day4.day4exception import *
import yaml

class TestYear(object):
    d4 = GetDays()
    def test_year_is_zero(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(0, 1, 1)
            self.d4.get_days()
        assert err_info.match( '输入的值小于0')

    def test_year_is_str(self):
        with pytest.raises(ValueError) as err_info:
            self.d4.get_date('teststr',1,1)
            self.d4.get_days()
        assert err_info.match('invalid literal for int()*')

    def test_year_is_minus(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(-2, 1, 1)
            self.d4.get_days()
        assert err_info.match('输入的值小于0')

class TestMonth(object):
    d4 = GetDays()
    def test_month_is_zero(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(2010,0,1)
            self.d4.get_days()
        assert err_info.match('输入的值小于0')

    def test_month_is_minus(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(2010,-2,1)
            self.d4.get_days()
        assert err_info.match('输入的值小于0')

    def test_month_is_str(self):
        with pytest.raises(ValueError) as err_info:
            self.d4.get_date(2010,'teststr',1)
            self.d4.get_days()
        assert err_info.match('invalid literal for int()*')

    def test_month_is_13(self):
        with pytest.raises(GreatThan12) as err_info:
            self.d4.get_date(2010,13,1)
            self.d4.get_days()
        assert err_info.match('输入的月份大于12')


class TestDay(object):
    d4 = GetDays()
    def test_day_is_zero(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(2010,0,1)
            self.d4.get_days()
        assert err_info.match('输入的值小于0')

    def test_day_is_minus(self):
        with pytest.raises(LowThanZero) as err_info:
            self.d4.get_date(2010,-2,1)
            self.d4.get_days()
        assert err_info.match('输入的值小于0')

    def test_day_is_31(self):
        with pytest.raises(GreatThan31) as err_info:
            self.d4.get_date(2010,1,32)
            self.d4.get_days()
        assert err_info.match('输入的日期大于31')

class TestToPass(object):
    d4 = GetDays()
    def test_20171231_365(self):
        self.d4.get_date(2017, 12, 31)
        days = self.d4.get_days()
        assert days==365

    def test_20171131_335(self):
        self.d4.get_date(2017, 11, 31)
        days = self.d4.get_days()
        assert days==335

    def test_20160228_59(self):
        self.d4.get_date(2016,2,28)
        days = self.d4.get_days()
        assert days ==59

    def test_20131001_274(self):
        self.d4.get_date(2013,10,1)
        days = self.d4.get_days()
        assert days == 274

    def test_20201231_366(self):
        self.d4.get_date(2020,12,31)
        days = self.d4.get_days()
        assert days ==366