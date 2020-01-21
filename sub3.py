#
# import time
# from datetime import date
#
#
#
#
#
# #print(time.strftime('%Y %m %d ',time.localtime(time.time())))
#
# #
#
# f_date = date(2019, 12, 21)
# print(f_date)


#!/usr/bin/python
#coding=UTF-8
import datetime

def getday(y=2017,m=8,d=15,n=0):
    the_date = datetime.datetime(y,m,d)
    result_date = the_date + datetime.timedelta(days=n)
    d = result_date.strftime('%Y-%m-%d')
    return d
#print(getday(2017,8,15,21) )#8月15日后21天
print(getday(2019,12,21,36))
print(getday(2019,12,21,81)) #9月1日前10天