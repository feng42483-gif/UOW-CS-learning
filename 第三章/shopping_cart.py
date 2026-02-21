from random import choice

shopping_cart = {}
menu = """
########购物车系统#########
#       1.添加购物车     #
#       2.修改购物车     #
#       3.删除购物车     #
#       4.查询购物车     #
#       5.退出购物车     #
########################
"""
print(menu)

while True:
    choice = input("请选择要执行的操作（1-5）：")
    match choice:
        case "1":
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")
        case "2":
            goods_name = input("请输入修改的商品名称：")
            goods_price = float(input("请输入最新的商品价格："))
            goods_num = int(input("请输入最新的商品数量："))
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改完毕")
        case "3":
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")
        case "4":
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称{goods_name}")
        case "5":
            print("拜拜")
            break
        case _:
            print("非法操作，不支持")


