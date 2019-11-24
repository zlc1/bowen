# sco = int(input("请输入你的分数:"))
# if sco >= 90 and sco <= 100:
#     print("优秀")
# elif sco >= 70 and  sco < 90:
#     print("一般")
# elif sco >= 60 and sco < 70:
#     print("及格")
# elif sco >= 0 and sco < 60:
#     print("不及格")
# else:
#     print("请输入有效成绩")

# a = 0
# i = 1
# while i <= 100:
#     a += i
#     i += 2
#
# print(a)

#
# a = 0
# for i in range(101):
#     if i % 2 == 1:
#         a += i
# print(a)
# a = int(input("请输入你的年龄："))
# if a >= 18:
#     print("网吧嗨皮")
# else:
#     print("回家写作业")
# a = [23,12,45,67,90]
# for i in
# 水仙花数
# a = 100
# while a <= 999:
#     b = a // 100
#     c = (a - b * 100) // 10
#     d = a - b * 100 - c * 10
#     if b ** 3 + c ** 3 + d ** 3 == a:
#         print(a,end=",")
#     a += 1
# 将二进制转化为十进制数
a = input("请输入一个数：")
b = a[::-1]
c = 0
for i in range(len(a)):
    d =int(b[i]*(2 ** i))
    c += d
print(c)



# Z同学为了实现暑假去云南旅游的梦想，决定以后每天只消费1元，每花k元就可以再得到1元，一开始Z同学有M元，问最多可以坚持多少天。
int
main(void)
{
    int
m, k, i, sum1, sum2;

while (scanf("%d%d", & m, & k) != EOF)
{
    sum1 = 0;
for (i = m; i >= 1; i --)
{
    sum1 + +;
if (sum1 % k == 0)
{
    i + +;
}

}
printf("%d\n", sum1);
}
return 0;
}

# a = int(input("请输入你花的钱："))
# if a % 3 == 1:
#     a += 1
# print("")
# def a():
#     a = 1
#     def b():
#         b = 2
#         print(b)
#         def c():
#             c = 3
#         return c
#     return b
# a()()()
# def hanshu():
# # a = 12
# #     print(a)
# #     def wrapper():
# #         b=254
# #         print(b)
# #         c = 25
# #         print(c)
# #
# #
# # return app
# # # wrapper()
# # return wrapper
# # # hanshu()()                            # 多个嵌套调用时，选择函数内数据下标位置
# # c = hanshu
# # c()()
# #
# #
# # def app():
# #
