has_ticket = int(input("请出示车票(1代表有，2代表没有:"))
if has_ticket == True:
    print("可以进行安检")
knife_length = int(input("请输入刀的长度"))
if knife_length >= 20:
     print("刀的长度 %d cm 不允许上车" % knife_length)
    else:
         print("安检通过")
else:
    print("请先购买车票")
a = int(input("请输入一个整数:"))
if a % 2 == 0:
    if a % 3 == 0:
        print("hello wrold")
    else :
        print("hello")
elif a % 3 == 0:
    print("world")
else:
    print("123")