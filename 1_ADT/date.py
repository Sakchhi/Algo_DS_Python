"""
Abstract Data Type to represent Date
Date represents a single day in the propletic Gregorian calendar. Max Date is November 24, 4714 BC

Interface:
Date(month, day, year) -- Constructor, date must be valid, BC dates have negative year
day, month, year -- Accessors returning specific date components
monthName
dayOfWeek
numDays(otherDate)
isLeapYear()
advanceBy(days)
comparable(otherDate) -- Compare to decide if >, <, >=, <=, ==, !=
toString -- Returns string representation
"""

from datetime import datetime, timedelta
class Date:

    def __init__(self, month, day, year):
        # self._julian_day = 0
        # print(month, day, year)
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."
        # tmp = 0
        # if month < 3:
        #     tmp = -1
        # self._julian_day = day - 32075 + \
        #                    (1461 * (year + 4800 + tmp) // 4) + \
        #                    (367 * (month - 2 - tmp * 12) // 12) + \
        #                    (3 * ((year + 4900 + tmp) // 100) // 4)
        DAY = timedelta(1)
        JULIAN_EPOCH = datetime(2000, 1, 1, 12)  # noon (the epoch name is unrelated)
        J2000_JD = timedelta(2451545)  # julian epoch in julian dates

        dt = datetime(year, month, day)  # get datetime object
        day_of_year = (dt - datetime(dt.year, 1, 1)) // DAY + 1  # Jan the 1st is day 1
        julian_day = (dt.replace(hour=12) - JULIAN_EPOCH + J2000_JD)//DAY
        self._julian_day = julian_day

    def month(self):
        return (self._toGregorian())[0]

    def day(self):
        return (self._toGregorian())[1]

    def year(self):
        return (self._toGregorian())[2]

    def day_of_week(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    def month_name(self):
        month = self._toGregorian()[0]
        MONTH_LIST = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        return MONTH_LIST[month-1]

    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    def __eq__(self, other_date):
        return self._julian_day == other_date._julian_day

    def __lt__(self, other_date):
        return self._julian_day < other_date._julian_day

    def __le__(self, other_date):
        return self._julian_day <= other_date._julian_day

    def _toGregorian(self):
        A = self._julian_day + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def is_leap_year(self):
        return False

    def _isValidGregorian(self, month, day, year):
        if month<1 or month > 12 or type(month) != int:
            return False
        if day < 1:
            return False
        else:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day > 31:
                    return False
                elif month in [4, 6, 9, 11]:
                    if day > 30:
                        return True
                else:
                    if Date(1,1,year).is_leap_year():
                        if day > 29:
                            return False
                    else:
                        if day > 28:
                            return False
        if year < -4713:
            return False
        return True

