#!/usr/bin/python
#-*-coding:utf8-*-
# 1.a =["abc","ABC","abb","cda"]
# 将列表以a或A开头，并且以c结尾的打印出来
a =["abc","ABC","abb","cda"]
for i in a:
#     if (i.startwith("a") or i.startwith("A")) and i.endswith("c"):
#         print(i)
    if (i[0] == "a" or i[0] == "A") and i[-1] == "c":
        print(a)
# # 2.b = [11,22,33,44,55,66,77,88,99]
# # 将大于55的放一起，小于55的放一起
# b = [11,22,33,44,55,66,77,88,99]
# c = []
# a = []
# for c in b:
#     if c > b[4]:
#         print(c)
# for a in b:
#     if a < b[4]:
#         print(a)
# a = input("请输入一个字符串：")
# if a.title():
#     print(a)
#     if a == "a":
#         a.replace("a")
# a = [12,346,123,543,123,543,345,543,345]
# for i in a:
#    if a.count(i) > 1:
#        for j in range(a.count(i)-1):
#         a.remove(i)
# print(a)
# a = [12,346,123,543,123,543,345,543,345]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# 三次猜数字
# import random
# while 1:
#     a =int(input("随机输入一个数字(1,10)："))
#     b = random.randint(1,10)
#     print("对比的数字为%d" %b)
#     if a > b:
#         print("提示大了")
#     elif a < b:
#         print("提示小了")
#     elif a == b:
#         print("猜对了")
#     else:
#         print("老子不玩了")
# 打印user1到user50
# for a in range(1,51):
#     print("user",a)
# 选择法：手动输入一组数据并排序
# a = "123"
# b = a.split(a)
# print(type(b))
# for i in range(len(b)-1):
#     for j in range(i+1,len(b)-1):
#         if a[j] < a[j + 1]:
#             a[j],a[j + 1] = a[j + 1],a[j]
#     print(a)










