# t = 0
# while t < 10:
#     print("循环")
#     t += 1
# # else:
# #     print("不循环")
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
# # print(f"1到100之内的所有偶数之和{total}")
# total = 0
# range(1,101,)
# for i in range(1,101):
# #     if i % 2 == 1:
# #         total += i
# # print(total)
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print(total)
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {i*j}",end="\t")
#     print()


# 案列1
# while True:
#     username = input("用户名：")
#     password = input("密码：")
#     if username == "" or password == "":
#         print("用户名或密码不能为空")
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功")
#         break
#     else:
#         print("出现错误，请重新登录")\


#
#
# # 案例2：
# import random
# random_num = random.randint(1, 100)
# while True:
#     num = int(input("请输入一个数字："))
#     if num > random_num:
#         print("数字大了")
#     elif num < random_num:
#         print("数字小了")
#     else:
#         print("猜对了")
#         break
# print(random_num)

# # 案例3
# total = 0
# range(1,1001)
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(total)

# # 案例4
# s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
#
# # 初始化计数器
# count_a = 0
# count_k = 0
#
# # 遍历字符串中的每一个字符
# for char in s:
#     if char == 'a':
#         count_a += 1
#     elif char == 'k':
#         count_k += 1
#
# print(f"a 的数量是: {count_a}")
# print(f"k 的数量是: {count_k}")

# # 案例5
# count = 0
# for i in range(1,501):
#     if i % 3 == 0 and i % 5 == 0:
#         count += 1
# print(count)

# # 案例6
# s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# count = {}
# for i in s:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(f"所有字符的统计结果：")
# print(count)
#
#
