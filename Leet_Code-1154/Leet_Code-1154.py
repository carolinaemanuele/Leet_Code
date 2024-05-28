'''
Question 1154
'''

class Solution:
    def dayOfYear(self, date: str) -> int:
        date = [int(x) for x in date.split('-')]
        leap_year = date[0]%4 == 0 and date[0]!=1900
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        if leap_year:
            days_in_month[1] = 29
        day = sum(days_in_month[:(date[1]-1)])+date[2]
        return day