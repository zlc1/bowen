#!/usr/bin/python
#-*-coding:utf8-*-
# a = 0
# for i in range(0,101,2):
#     a += i
# print(a)
# a = 0
# for i in range(0,101,1):
#     a += i
# print(a)
# for i in "abcde":
#     if i == "c":
#         continue
#     print(i)
# for i in "abcd":
#     if i == "c":
#         break
#     print(i)
# for i in "abcde":
#     if i == "c":
#       break
#     else:
#         print("ifif")
#     print(i)
# else:
#     print("这个循环结束了")
# for i in "abc":
#     print(i)
#     for j in "def":
#         print(j)
# a = 0
# # b = 0
# # for i in range(5):
# #     a += 1
# #     for j in range(1):
# #         b = 5
# # print(a,b)
a = 0
for i in range(1,100):
    if i % 2 == 0:
        a -= i
    else:
        a += i
print(a)
