#!/usr/bin/python

""" Sample Codes of Chapter 3, <Python Cookbook> """

import datetime
import calendar
import time
from dateutil import rrule

### Calculating yesterday and tomorrow
def s3_1 ():
    today = datetime.date.today( )
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print yesterday, today, tomorrow

### Finding last Friday
def s3_2_1 ():
    lastfriday = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    while lastfriday.weekday() != calendar.FRIDAY:
        lastfriday -= oneday
        print lastfriday.strftime('%A, %d-%b-%Y')

def s3_2_2 ():
    today = datetime.date.today()
    targetday = calendar.FRIDAY
    thisday = today.weekday()
    deltatotarget = (thisday - targetday) % 7 # clever way
    lastfriday = today - datetime.timedelta(days=deltatotarget)
    print lastfriday.strftime('%A, %d-%b-%Y')


def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

### repeatly execute command
def s3_10 ():
    for i in range(3):
        print i
        time.sleep(2)

### schedule a command
def s3_11 ():
    none

### Decimal Arithmetic
def s3_12 ():
    f = 0.3
    print f / 3 # 0.0999999... in console
    import decimal
    d = decimal.Decimal("0.3")
    print d / 3

if __name__=='__main__':
    starts = [datetime.date(2005, 01, 04), datetime.date(2005, 01, 03)]
    end = datetime.date(2005, 01, 10)
    s3_12()
    for s in starts:
        days = rrule.rrule(rrule.DAILY, dtstart=s, until=end).count( )
        print "%d days shows as %d weeks "% (days, weeks_between(s, end))

