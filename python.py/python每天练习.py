#!/usr/bin/python
#-*-coding:utf8-*-
# 1.简述：这里有四个数字，分别是：1、2、3、4
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# def aa():
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a != b and b != c and  a != c:
#                 print("%s%s%s" %a,b,c)
#
# aa()
# """
# 我国现有13亿人口，设每年增长0.8%，编写程序，计算多少年后达到26亿
a = 13
b = 0
while 1:
    if a >= 26:
        break
    a = a * (1 + 0.008)
    b += 1
print(b)
#
# # bb()
# # # 两个小组对战，对战规则如下：a 不和x对战，b 不和y,z 对战
# # t1 = ["a","b","c"]
# # t2 = ["x","y","z"]
# # for i in t1:
# #     for j in t2:
# #         if i == "a" and j == "x":
# #             continue
# #         elif  i == "c" and (j == "y" or j =="z"):
# #             continue
# #         else:
# #             print("%s VS %s"%(i,j))
# 2.循环删list元素

# li = [1,1,2,3,4,5,6,7,8,9]
# for i in li:
#     if i % 2 != 0:
#         li.remove(i)
#     print(li)
# 利用循环语句输出1到50中5的倍数，将其存放到一个列表中。
# a = []
# for i in range(1,51):
#     if i % 5 == 0:
#         a.append(i)
# print(a)

# . 计算10个99相加后的值并输出。
# a = 0
# b = 0
# c = 99
# while a < 10:
#         b += c
#         a += 1
# print(b)
# a = 0
# for i in range(10):
#     a += 99
# print(a)
# 计算100 - 999 的水仙花数
# for a in range(100,1000):
#      b = a // 100
#      c = (a - b * 100) // 10
#      d = a - b * 100 - c * 10
#      if b ** 3 + c ** 3 + d ** 3 == a:
#              print(a,end=",")
#  已知-个列表存储了多个整数，请编写函数,删除列表中的素数。


# 37,7,91,67
# 7,27,45,6]
# 2
# arrl = [12,3,3
# [12,3,37,7,
# 91 ,67,27,45,6]
# 3
# arr2 =
# 4
# def delPrime(
# (arr1):
# for element in arr2:
# 5
# #质数大于1
# if element > 1:
# 7
# #查看因子
# 8
# fori in range(2, elenent):
# = 0:
# 9
# if (element % 1)
# 10
# break
# 11
# else:
# 12
# arr1. remove(
# element)
# 13
# 14
# delPrime(arr1)
# 15 | print(arr1)
# 字典排序

# dic={'a':1,'c':3,'b':2,'d':4}
# print(dic)
# dic=sorted(dic.items())
# print(dic)
# 元素分类
# 有如下值集合[11, 22, 33, 44, 55, 66, 77, 88, 99, 90]，将所有大于
# 66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
# 即: {'k1': 大于 66 的所有值, 'k2': 小于 66 的所有值}
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# a = []
# b = []
# for i in li:
#     if i > 66:
#         a.append(i)
#     else:
#         b.append(i)
# dict = {"k1": a, "k2": b}
# print(dict)
# 找出六位数中的回文数，打印并计算个数。
# for i in range(10000,100000):
#     a=str(i)
#     if a[0]==a[4] and a[1]==a[3]:
#         print(a)









