


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
num = 100
def cycle_area(r):
    pi = 3.14
    area = pi * r * r
    global num
    num = 10000
    print(num)
    return area
c_area = cycle_area(num)
print(c_area)
print(num)