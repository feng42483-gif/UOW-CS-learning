# 特点：无序，不可重复，可修改
import pprint

s = {12,13,23,45,67,89}
s1 = {12,14,18,23,45,69,87,89}
# print(s)
# print(type(s))

# 向该集合添加元素
# s.add(14)
# print(s)

# 去除指定元素
# s.remove(45)
# print(s)

# 随机删除一个元素并返回
# s.pop()
# print(s)

# 清空集合
# s.clear()
# print(s)

# 两个集合的差集,第一个集合减第二个集合
# s.difference(s1)
# print(s.difference(s1))
# 差集的第二种表达方式
# s2 = s-s1
# print(s2)
# 差集集合推导式
# s2 = {s2 for s2 in s if s2  not in s1}
# print(s2)



# 并集
# s.union(s1)
# print(s.union(s1))
# 并集的第二种表达方式
# s2 = s|s1
# print(s2)


# 交集
# s.intersection(s1)
# print(s.intersection(s1))
# 交集的第二种表达方法
# s2 = s & s1
# print(s2)


