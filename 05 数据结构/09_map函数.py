# 09 映射函数

items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# 将这个列表转换为只包含价格的简单列表
# prices = []
# for index in items:
#     prices.append(index[1])
# print(prices)

# 使用 map() 函数可以更简洁地实现相同效果
prices = map(lambda index: index[1], items)
print(prices) # map 对象（可迭代）
for index in prices:  # 遍历 map 对象
    print(index)

# 如果需要直接得到列表，可以用 list() 转换
prices = list(map(lambda index: index[1], items))
print(prices)



# 这就是映射函数的用法，传入一个匿名函数，将他应用于这个可枚举对象中的每个item元素

# for example


def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
# map函数应用
result = map(square, numbers)
print(result)         # <map object at 0x...> 迭代器对象
print(list(result))   # [1, 4, 9, 16, 25]



# 与上面相同

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x + 10, numbers) # 这就是映射函数的用法，传入一个匿名函数，将他应用于这个可枚举对象中的每个item元素
print(list(result))  # [11, 12, 13, 14, 15]
