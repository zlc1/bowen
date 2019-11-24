#!/usr/bin/python
#-*-coding:utf8-*-
# def hanshu():
#     print("nihao1")
# def hanshu1():
#     print("you are very good")

# try:
#     a = "asd"
#     str(a)
#     print("执行了try语句")
# except Exception as f:
#     print(f,"执行了except语句")
# else:
#     print("执行了els语句")
# finally:
#     print("执行了finally语句")
# except ValueError as b:
#     print(b)
# print(123)
# raise TypeError("hi")
# print(123)
# a =["sd","sd"]
# a.append("ds")
# print(a)
# b = ["sd","uyu"]
# b.insert(0,"e")
# print(b)
"字符串"

# a = "qwqeq"
# # a.upper()
# # print(a.upper())
# a = "ASS"
# a.lower()
# print(a.lower())
# a = "das"
# a.title()
# print(a.title())
# a = "ads".endswith("a")
# print(a)
# a = "sdsda".startswith("s")
# print(a)
# a = ["dsd","fef"]
# b = "-".join(a)
# print(b)
# a = "sdsd"
# b = a.swapcase()
# print(b)
# a = "dwsdw"
# b = a.split("s")
# print(b)
# a = "dsdwdsdw"
# b = a.replace("s","a",1)
# print(b)
# a = "asdwwsasda"
# b = a.strip("asd")
# print(b)
# a = "asdasd"
# b = a.count("a")
# print(b)
# a = "adsddsdd"
# b = len(a)
# print(b)
# "列表"
# 1.append
# 2.extend
# 3.insert
# 4.clear
# 5.remove
# 6.reversed
# 7.srot(reverse = true)
# a = ["dasdd"]
# b = a.append(2,)
# print(b)
# a = "dad"
# b = "123"
# b.extend(a)
# "元组"
# 1.count
# 2.index
# "字典"
# 1.popitem
# 2.keys
# 3.values
# 4.items
# 5.sort
# 6.update
# a = {"name":"12","age":"14"}
# b = {}
# b.update(a)
# print(b)
try:
    a = "ds"
    int(a)
    raise TypeError("这是类型错误")
except Exception as e:
    print(e)