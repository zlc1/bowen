#!/usr/bin/python
#-*-coding:utf8-*-
# 1.九九乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#         k = i * j
#         print('%d*%d=%d'%(j,i,k),end='\t')
#     print()
# 2.	质数之和（任意范围的）
# a = 2
# c = 0
# while a < 101:
#     b = 2
#     while b < a:
#         if a % b == 0:
#             break
#         b += 1
#     else:
#         c = c + a
#     a += 1
# print(c)
# 3.阶乘之和
a = int(input("请输入一个数："))
b = 1
c = 0
i = 1
while a >= i:
    b = b * i     #阶乘的乘积
    c = c + b     #阶乘的和
    i += 1
print(c)


#7.判断字符串是否是回文
#9.三次猜数字
a =


# 10.水仙花数
# a = 100
# while a <= 999:
#     b = a // 100
#     c =( a - 100 * b) // 10
#     d = a - 100 * b - 10 * c
#     if b ** 3 + c ** 3 + d ** 3 == a:
#         print(a)
#     a += 1
# high = 10
# up = 2
# down = 1
# 13.任意4个数字，组成不相同的三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and j != k and i != k:
#                 print("%s%s%s" %(i,j,k))

#23.青蛙跳
# high = int(input("井深的高度："))
# up = int(input("向上爬的高度："))
# down = int(input("向下滑的高度："))
# day = 0
# while 1:
#     high -= up
#     high += down
#     if high == 0:
#         break
#     day += 1
# print("%s天" %day)
import random
from time import sleep
#定义一个随机数
answer=random.randint(1,100)
print("You have only 3 chances!")
sleep(3)
print("READY,GO!!!")

#判断是否猜想正确
for i in range(1,4):
    i = i + 1
    # 定义一个猜想数，在1-100之间
    n = int(input("input an number:"))
    if n==answer:
        print("Bingo! You are right!!!")
        break
    elif n>answer:
        print("number > answer!Play again!\n")
    else :
        print("number < answer!Play again!\n")
print('GAME OVER!!!')
# ————————————————
# 版权声明：本文为CSDN博主「Taxus_shan」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Taxus_shan/article/details/90208323

