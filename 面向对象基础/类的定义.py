# 定义类
# class 类名:(类名命名规范，每个单词的首字母都大写，单词之间没有间隔符)
#     pass
# 创建对象
# 对象名  = 类名()
# 对象名.属性名1 = 属性值1
#对象名.属性名2 = 属性值2

# 列
# class Car:
#     pass
# c1 = Car()
# c1.brand = "BWM"
# c1.name = "X5"
# c1.price = 60000
# print(c1.__dict__)

# 定义类2
# class Car:
#     def __init__(self ,brand,name,price):
#         self.brand = "BWM"
#         self.name = "X5"
#         self.price = 50000
# c1 = Car("BWM","X5",5000)
# print(c1.__dict__)



# 定义类，实例方法
# class Car:
#     def __init__(self, brand,name,price):
#         self.brand = brand
#         self.name = name
#         self.price = price
#
#     def running(self):
#         print(self.brand,self.name,self.price)
#
#     def total_cost(self,discount,rate):
#         total = discount * rate * self.price
#         return total
#
# c1 =Car("BWM","X7",70000)
# c1.running()
# tota = c1.total_cost(discount=0.2,rate=0.5)
# print(tota)



# 魔法方法：指python提供的以下划线开头结尾的特殊方法eg。__init__


# class Car:
#     def __init__(self, brand,name,price):
#         self.brand = brand
#         self.name = name
#         self.price = price
#
#     def running(self):
#         print(self.brand,self.name,self.price)
#
#     def total_cost(self,discount,rate):
#         total = discount * rate * self.price
#         return total
#
#     def __str__(self):
#         return f"{self.brand} {self.name} {self.price}"
#
#     def __eq__(self, other):
#         return self.brand == other.brand and self.name == other.name and self.price == other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
# c1 =Car("BWM","X7",70000)
# c2 = Car("BYD","汉",30000)
# print(c1 == c2)
# print(c1 > c2)