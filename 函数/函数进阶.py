


# # 全局变量与局部变量
# num = 100
# def cycle_area(r):
#     pi = 3.14
#     area = pi * r * r
#     return area
# c_area = cycle_area(num)
# print(c_area)

# 局部变量
# num = 100
# def cycle_area(r):
#     pi = 3.14
#     area = pi * r * r
#     # global num
#     num = 10000
#     print(num)
#     return area
# c_area = cycle_area(num)
# print(c_area)
# print(num)

# 全局
# num = 100
# def cycle_area(r):
#     pi = 3.14
#     area = pi * r * r
#     global num
#     num = 10000
#     print(num)
#     return area
# c_area = cycle_area(num)
# print(c_area)
# print(num)

# 传参方式
# # 关键字参数
# def reg_stu(name,age,gender,city):
#     print(f"姓名:{name},{age},{gender},{city}")
#     return {name,age,gender,city}
# stu = reg_stu(name="张三", age=13, gender="男",city ="北京")
# print(stu)

#
# # 位置参数
# def reg_stu(name,age,gender,city):
#     print(f"姓名:{name},{age},{gender},{city}")
#     return {name,age,gender,city}
# reg_stu("张三","16","男","北京")

#
# # 位置参数+关键字参数  位置参数在前，关键参数在后
# def reg_stu(name,age,gender,city):
#     print(f"姓名:{name},{age},{gender},{city}")
#     return {name,age,gender,city}
# reg_stu("张三","16",gender="男",city="北京")
#
# # 默认参数
# def reg_stu(name,age,gender="男",city="深圳"):
#     print(f"姓名:{name},{age},{gender},{city}")
#     return {name,age,gender,city}
# reg_stu("王琳", 13)

# # 不定长参数-元组
# def calculate_data(*arge):
#     min_data = min(arge)
#     max_data = max(arge)
#     avg_data = sum(arge)/len(arge)
#     return min_data, max_data, round(avg_data,1)
# min_data, max_data, avg_data = calculate_data(1,5,8,10,578)
# print(min_data, max_data, avg_data)
#
# # 不定长参数-关键字参数*kwarg
# def calculate_data(*arge,**kwargs):
#     min_data = min(arge)
#     max_data = max(arge)
#     avg_data = sum(arge)/len(arge)
#     if kwargs.get("round") is not None:
#         avg_data = round(avg_data, kwargs.get("round"))
#     if kwargs.get("print"):
#         print({avg_data,min_data,max_data})
#
#     return min_data, max_data, round(avg_data,1)
# min_data, max_data, avg_data = calculate_data(1,5,8,10,578,round=3,print=True)
#


# 函数参数类型
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# def calc (a,b,oper):
#     return oper(a,b)
# result = calc(10,20,oper=divide)
# print(result)


# 匿名函数
# a = lambda : print("hello")
# a()
# add = lambda x, y: x + y
# print(add(10, 20))

# 按照字符个数排序
# data_list =["C++","Python","Java","C#","JavaScript"]
# 调用lambda函数，len为内置函数 reverse为反转，默认为false
# data_list.sort(key=lambda item :len(item), reverse = True)
# print(data_list)

# 类型注解
def circle_area(r: float) -> float:
    area = 3.14 * r ** 2
    return area
area = circle_area(10)
print(area)