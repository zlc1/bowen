#!/usr/bin/python
#-*-coding:utf8-*-
# second = time.time()
# print(second)
# shiJian = time.localtime()
# print(shiJian)
# print(type(shiJian))
# utc_shiJian = time.gmtime()
# print(utc_shiJian)
# local = time.localtime(0)
# print(local)
# Utc = time.gmtime(0)

import time
#将结构化转化为格式化时间,以字符串的格式显示
# geShiHua = time.strftime('%Y-%m-%d-%W %X',time.localtime())
# print(geShiHua)
# gSH = time.strftime('')
# #将格式化时间转华为结构化转化
# shiJian = time.strptime('2019-10-29-43 09:56:39','%Y-%m-%d-%W %X')
# print(shiJian)
# jieGuoHua = time.strptime('2019-10-28 18:00:00','%Y-%m-%d %X')
# shiJian = time.mktime(jieGuoHua)
# print(shiJian)

# geShiHua = time.strftime('%Y-%m-%d %X',time.localtime())
#
# shi_jian = time.localtime()
# # print(shi_jian)
# a = (2019,10,29,10,29,8,1,302,0)
# b = time.mktime(a)
# print(b)

#sellp()休眠时间
# from time import *
# start = time()
# for i in range(6):
#     print(i)
#     sleep(4)
# end = time()
# print('代码执行的时间为%f' %(end - start))
#随便输入一个年份判断是否是闰年
#①、普通年能被4整除且不能被100整除的为闰年。②、世纪年能被400整除的是闰年
# a = int(input('请输入年份：'))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('闰年')
# else:
#     print('平年')
