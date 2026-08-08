# 商品类
class Good:
    def __init__(self,name,number,price):
        self.name = name
        self.number = number
        self.price = price

    def __str__(self):
        return f"名称：{self.name},商品数量：{self.number},价格：{self.price}"


    def update_info(self,number = None, price = None):
        if number is not None:
            self.number = number
        if price is not None:
            self.price = price


# 购物车管理系统
class Shopping:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self,):
        self.good_list = []

    def add_good(self):
        name = input("请输入商品姓名：")
        for s in self.good_list:
            if s.name == name:
                print("该商品已存在")
                return



        number = int(input("请输入商品数量："))
        price = int(input("请输入商品价格："))

        if number >= 0 and price >= 0:
            good_message = Good(name,number,price)
            self.good_list.append(good_message)
            print("商品信息已添加")
        else:
            print("商品信息错误，价格，数量必须是非负数")

    def update_good(self):
        name = input("请输入要修改的商品名称")
        for s in self.good_list:
            if s.name == name:
                print(f"商品当前信息{s}")

                number = int(input("请输入要修改的商品数量："))
                price = float(input("请输入要修改的商品价格："))
                if number >= 0 and price >= 0:
                    s.update_info(number,price)
                    print("商品添修改成功")
                    print(f"商品修改后的信息为{s}")
                    return
                else:
                    print("商品信息错误，价格，数量必须是非负数")
                    return
        print("未找到该商品，修改失败")


    def delete_good(self):
        name = input("请输入要删除的商品名称")
        for s in self.good_list:
            if s.name == name:
                self.good_list.remove(s)
                print("删除成功")
                return

        print("未找到，删除失败")

    def find_good(self):
        name  = input("请输入要查询的商品名称")
        for s in self.good_list:
            if s.name == name:
                print(f"该商品的信息{s}")
                return
        print("该商品未找到")


    def run(self):
       print(f"该商品的版本号为V{Shopping.system_version}】")
       while True:
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
           choice = input("请选择要执行的操作（1-5）：")
           match choice:
               case "1":
                   self.add_good()
               case "2":
                   self.update_good()
               case "3":
                   self.delete_good()
               case "4":
                   self.find_good()
               case "5":
                   print("bye")
                   break
               case _ :
                    print("输入错误")


if __name__ == "__main__":
    going = Shopping()
    going.run()




