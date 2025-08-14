# 10 筛选函数

items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)
# 另一个使用 lambda 函数的场景：
# 过滤这个列表，只获取价格大于等于 10 的商品
filtered_price = list(filter(lambda index: index[1] >= 10, items))
print(filtered_price)
