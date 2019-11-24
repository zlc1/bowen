#!/usr/bin/python
#-*-coding:utf8-*-
# 计算10以内的平方和，并把它放在列表中
# a = []
# for i in range(2,11,2):
#     a.append(i ** 2)
# print(a)
#
#
# b = [i ** 2 for i in range(2,11,2)]
# print(b)
# a = [11,22,33,44,55,66,77,88,99]
# # b = [i for i in a if i > 55]
# # c = [i for i in a if i < 55]
# # print(b)
# # print(c)
# # a = [11,22,33,44,55,66,77,88,99]
# # b = sum(range(101))
# # print(b)
# print(sum(range(2,101,2)))
# a = [11,22,33,44,55,66,77,88,99]
# def jiujiu():
#     for a in range(1,10):
#         for i in range(1,a+1):
#             print("%d * %d = %d" % (a, i, a * i), end="\t")
#         print("")
#
#
#
# jiujiu()
#
#
#
#
#
#
#
#
#
# jiujiu()
#
#
#
#
# jiujiu()




# def 一到一百的和():
#     a = 0
#     for i in range(1,101):
#         a += i
#     print(a)
#
#
#
#
# 一到一百的和()
#
#
#
#
#
#
#
#
#
#
# 一到一百的和()
# def aaa():
#     gloabal = 2
#     a = 3
#     print(a)
#
#
#
# aaa()
#
#
#
#
# aaa()
# def a():
#     print(sum(range(1,101)))
#
#
#
#
#
# a()
# 1 - 2 + 3 - 4 + 99...
# 参数传递
# def sum(x,y):
#     a = 0
#     for i in range(x,y + 1):
#     print(a)
#
# sum(x,y)
# def sum(x = 2 ,y = 100 ):
#     a = 0
#     for i in range(x,y+1):
#         b = [j for j in range (2,i) if i % j == 0]
#         if len(b) == 0:
#             a += i
#     print(a)
#
# sum(123,13132)



# def sum1(x):
#     b = sum(range(x + 1))
#     return b
# def sum2(x):
#     for i in range(2,x+1):
#         b = [j for j in range (2,i) if i % j == 0]
#         if sum(b) == i:
#             print(i)
# c = sum1(100)
# print(c)
# # aa()
# def sum(**x):
#     print(x)
#
#
# sum({123})
# 一个函数，传两个参数a，b，a是列表，b是一个数字，找出a列表中两数之和等于b，打印出来这两个数。
def a(x, y=[]):
    for i in range(len(y)):
        for j in range(i + 1, len(y)):
            if y[i] + y[j] == x:
                print(y[i], y[j], x)


a(13,[12,1,11,2])












