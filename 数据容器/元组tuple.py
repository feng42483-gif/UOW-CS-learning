# 特点可以存储不同类型的元素，存储的元素可重复，有序但（不可被修改），支持索引访问和切片
from itertools import count

# s = (13,23,45,67,31,13)
# print(type(s))

# print(s[:3:])

# 累计指定元素的个数
# print(s.count(13))

# 指出目标索引位置
# print(s.index(13))


# 定义单元素元组需要在元素后加逗号,
# a = (100,)
# print(type(a))

# 定义元组组包
# t1 = (1,3,4,5,6,7,8)
# t1 = 1,2,3,4,5,6,7,8

# 解包
# 1.基础解包
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)

# 2.(*)扩张解包,*该符号会接受剩余元素并组成list
# x,*y,z = t1
# print(x)
# print(y)
# print(z)

# 两个值互换运用元组解包和组包操作即可实现
# a = 10
# b = 20
# a,b = b,a
# print(b,a)
#
# a =100
# b =200
# c =300
# a,b,c = b,c,a
# print(a,b,c)