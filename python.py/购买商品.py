#!/usr/bin/python
#-*-coding:utf8-*-
# 功能要求:
# ●要求用户输入总资产，例如: 2000
# # ●显示商品列表，让用户根据序号选择商品，加入购物车
# # ●,购买如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# # 附加:可充值、某商品移除购物车
# goods = [
#     { "name": "电脑", "price": 1999},
#     {"name": "鼠标”， "price": 10},
#     {"name": "美女"，"price": 998},
#     {"name": "美女"，"price": 998},
# total_assets = int(input("请输入你的总资产："))
# while 1:
#     print("显示商品的列表：")
goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
total_wages = int(input("请输入工资:")) #输入的工资
shop_cart = {}
for i in enumerate (goods):
    print(i)
while True:
    choice = input("请选择购买的商品：")
    if choice.lower() == "y":
        break
    for item in goods:
        if item[i] == choice:
            i = item[goods]
            if i in shop_cart.keys():
                shop_cart[i]["num"] = shop_cart[i]["num"] + 1
            else:
                shop_cart[i] = {"num":1,"single_price":item["price"]}
    print(shop_cart)
sum_price = 0
for k,v in shop_cart.items():
    t_price = v["single_price"]*v["num"]
    print("购买%s的数量为%s:总价为%d"%(k,v["num"],t_price))
    sum_price=sum_price+t_price
print("所有商品总价为:%s"%sum_price)
if sum_price>total_wages:
    print("’钱不够")
else:
    print("购买成功")

