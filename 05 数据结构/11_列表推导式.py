# 11 列表推导式

products = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(products)

# 使用 map 获取价格列表
# prices = list(map(lambda item: item[1], products))
# print(prices)

prices = [item[1] for item in products] # 使用列表推导式可以更简洁地实现相同功能
print(prices)

# 使用 filter 获取价格大于等于 10 的商品
# filtered_price = list(filter(lambda item: item[1] >= 10, products))
# print(filtered_price)

# 使用列表推导式实现相同功能
filtered_price = [item for item in products if item[1] >= 10]
print(filtered_price)


# 思想
# 使用中括号定义一个列表，然后写一段推导式（表达式+类似于for循环遍历表达式中每一个元素），