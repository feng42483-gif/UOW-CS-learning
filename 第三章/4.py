# 判断奇偶
# num = int(input("数字："))
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
# 判断年龄
# year = int(input("年龄"))
# if year >=18:
#     print("成年")
# else:
#     print("未成年")
#判断正负
# num = int(input("数字："))
# if num > 0:
#     print("正数")
# else:
#     print("负数")
#判断及格
# num = int(input("成绩："))
# if num > 60:
#     print("及格")
# else:
#     print("不及格")
# if.....elif...else
# num = int(input("数字："))
# if num >0:
#     print("正数")
# elif num < 0:
#     print("负数")
# else:
#     print("0")
# account = input("账户")
# password = input("密码")
# if account == "admin" and password == "666888":
#     print("登录成功")
# elif account == "root" and password == "547527":
#     print("登录成功")
# elif account == "zhang san" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")
# num = int(input("成绩："))
# if num >85:
#     print("优秀")
# elif num <=85 and num >=60:
#     print("及格")
# else:
# #     print("不及格")
# num = int(input("金额:"))
# if num >=500:
#     print("八折优惠")
# elif 300 <= num < 500:
#     print("九折")
# elif 100<= num < 300:
#     print("95折")
# else:
#     print("无折扣")
# 三角形判断
# a = int(input("第一个边长:"))
# b = int(input("第二个边长:"))
# c = int(input("第三个边长:"))
# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("等边三角形")
#     elif a == b or b == c or a == c:
#         print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不是三角形")
 # 计算电费 ,
# total = 0
# if num <= 2880:
#     total = num * 0.4883
# elif num <= 4800:
#     total = (2880 * 0.4883) + (num - 2880) * 0.5383
# else:
#     total = (num * 0.4883) + (4800 - 2880) * 0.5383 + (num - 4800)* 0.7883
# print(f"您的年度总电费：{total:.2f}元")
# # # 1. 输入用电数
# usage = float(input("请输入年度用电量（度）："))
#
# # 2. 初始化电费变量
# total_bill = 0
#
# # 3. 使用 if-elif-else 进行阶梯逻辑判断
# if usage <= 2880:
#     # 仅在第一档
#     total_bill = usage * 0.4883
# elif usage <= 4800:
#     # 进入第二档：前2880度 + 超过的部分
#     total_bill = (2880 * 0.4883) + (usage - 2880) * 0.5383
# else:
#     # 进入第三档：前2880度 + 第二档2880-4800的部分 + 超过4800的部分
#     total_bill = (2880 * 0.4883) + (4800 - 2880) * 0.5383 + (usage - 4800) * 0.7883
#
# # 4. 输出结果（保留两位小数）
# print(f"您的年度总电费为：{total_bill:.2f} 元")
