# # 19 Dictionaries

# Python 内置的另一种非常有用的数据类型是字典（dict）。
# 字典在其他语言中有时被称为“关联数组”或“映射”。
# 与按数字索引的序列不同，字典是按键（key）索引的，键可以是任何不可变类型。
# 字符串和数字总是可以作为键，元组也可以作为键（前提是元组中只包含不可变类型）。
# 如果元组中包含可变对象（直接或间接），就不能作为键。
# 列表不能作为键，因为列表可以被原地修改。
# 可以把字典看作一组 key:value（键值对），且键必须唯一。
# 使用 {} 创建空字典；在花括号中添加以逗号分隔的键值对可以直接创建字典。
# 主要操作包括：为某个键存储值、通过键取值、删除键值对。
# 如果使用已存在的键存储值，会覆盖原值。
# 如果通过不存在的键取值会报错，可以用 get() 方法避免报错。
# list(d) 会返回字典的所有键（按插入顺序），如果要排序可用 sorted(d)。
# 用 in 关键字可以检查字典中是否存在某个键。

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # 使用 dict() 函数创建字典
print(point)

print(point["x"])  # 使用键访问值

point["x"] = 10  # 修改键 "x" 对应的值
print(point)

point["z"] = 3  # 添加新的键 "z" 及其值
print(point)

# 检查键是否存在
if "a" in point:
    print("yes")
else:
    print("no")

# 使用 get() 方法获取键的值，如果不存在返回 None（不会报错）
print(point.get("a"))

# 删除键（示例）
# del point["x"]

print(point)

# 遍历字典的键
for key in point:
    print(key)

# 遍历字典的键和值
for key in point:
    print(key, point[key])

# 遍历字典的项（返回元组）
for index in point.items():
    print(index)

# 通过解包同时获取键和值
for key, value in point.items():
    print(key, value)

# 查看所有键值对.
print(point.items())

# 转为列表
print(list(point.items()))

# 获取所有值并转为元组
print(tuple(point.values()))

# python中只能使用可枚举类型作为键，大部分使用字符串，值可以为任何类型没有限制，建立字典的方法
# 可以通过序号访问字典内的元素，这里的序号指的是一个键值对的键，因为字典是键值对的集合，不可以使用一个数字的索引来访问，与列表不同