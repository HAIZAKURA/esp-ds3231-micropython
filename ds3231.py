""" 
DS3231 RTC Drive
Author: HAIZAKURA
For: ESP8266 / ESP32
2019.March
""" 

import machine
from machine import I2C, Pin
from micropython import const

DS3231_ADDRESS          = const(0x68)
DS3231_SEC_REG          = const(0x00)
DS3231_MIN_REG          = const(0x01)
DS3231_HOUR_REG         = const(0x02)
DS3231_WDAY_REG         = const(0x03)
DS3231_MDAY_REG         = const(0x04)
DS3231_MONTH_REG        = const(0x05)
DS3231_YEAR_REG         = const(0x06)
DS3231_AL1SEC_REG       = const(0x07)
DS3231_AL1MIN_REG       = const(0x08)
DS3231_AL1HOUR_REG      = const(0x09)
DS3231_AL1WDAY_REG      = const(0x0A)
DS3231_AL2MIN_REG       = const(0x0B)
DS3231_AL2HOUR_REG      = const(0x0C)
DS3231_AL2WDAY_REG      = const(0x0D)
DS3231_CONTROL_REG      = const(0x0E)
DS3231_STATUS_REG       = const(0x0F)
DS3231_AGING_OFFSET_REG = const(0x0F)
DS3231_TMP_UP_REG       = const(0x11)
DS3231_TMP_LOW_REG      = const(0x12)

class DS3231(object):
    def __init__(self, sdapin, sclpin):
        self.i2c = I2C(sda=Pin(sdapin), scl=Pin(sclpin), freq=100000)

    def dec2hex(self, dat):
        res = (int(dat / 10) << 4) + (dat % 10)
        return res

    def get_reg(self, reg):
        buf = bytearray(1)
        buf[0] = reg
        self.i2c.writeto(DS3231_ADDRESS, buf)
        rev = self.i2c.readfrom(DS3231_ADDRESS, 1)[0]
        res = (rev >> 4) * 10 + (rev % 16)
        return res

    def set_reg(self, dat, reg):
        buf = bytearray(2)
        buf[0] = reg
        buf[1] = dat
        self.i2c.writeto(DS3231_ADDRESS, buf)

    def hour(self, hour=''):
        if hour == '':
            return self.get_reg(DS3231_HOUR_REG)
        else:
            self.set_reg(self.dec2hex(hour), DS3231_HOUR_REG)

    def min(self, min=''):
        if min == '':
            return self.get_reg(DS3231_MIN_REG)
        else:
            self.set_reg(self.dec2hex(min), DS3231_MIN_REG)

    def sec(self, sec=''):
        if sec == '':
            return self.get_reg(DS3231_SEC_REG)
        else:
            self.set_reg(self.dec2hex(sec), DS3231_SEC_REG)

    def year(self, year=''):
        if year == '':
            return self.get_reg(DS3231_YEAR_REG) + 2000
        else:
            self.set_reg(self.dec2hex(year - 2000), DS3231_YEAR_REG)

    def month(self, month=''):
        if month == '':
            return self.get_reg(DS3231_MONTH_REG)
        else:
            self.set_reg(self.dec2hex(month), DS3231_MONTH_REG)

    def day(self, day=''):
        if day == '':
            return self.get_reg(DS3231_MDAY_REG)
        else:
            self.set_reg(self.dec2hex(day), DS3231_MDAY_REG)

    def time(self, hour='', min='', sec=''):
        if hour == '' or min == '' or sec == '':
            res = []
            res.append(self.hour())
            res.append(self.min())
            res.append(self.sec())
            return res
        else:
            self.hour(hour)
            self.min(min)
            self.sec(sec)

    def date(self, year='', month='', day=''):
        if year == '' or month == '' or day == '':
            res = []
            res.append(self.year())
            res.append(self.month())
            res.append(self.day())
            return res
        else:
            self.year(year)
            self.month(month)
            self.day(day)

    def datetime(self, year='', month='', day='', hour='', min='', sec=''):
        if year == '' or month == '' or day == '' or hour == '' or min == '' or sec == '':
            res = []
            res.append(self.year())
            res.append(self.month())
            res.append(self.day())
            res.append(self.hour())
            res.append(self.min())
            res.append(self.sec())
            return res
        else:
            self.year(year)
            self.month(month)
            self.day(day)
            self.hour(hour)
            self.min(min)
            self.sec(sec)

    def temp(self):
        buf = bytearray(2)
        buf[0] = DS3231_TMP_UP_REG
        buf[1] = DS3231_TMP_LOW_REG
        self.i2c.writeto(DS3231_ADDRESS, buf)
        rev = self.i2c.readfrom(DS3231_ADDRESS, 2)
        if rev[0] > 0x7F:
            return rev[0] - rev[1] / 256 - 256
        else:
            return rev[0] - rev[1] / 256
