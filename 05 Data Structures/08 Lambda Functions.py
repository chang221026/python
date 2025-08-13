# 08 Lambda（匿名函数）

# 复杂对象的列表，例如元组列表（订单包含商品名和价格）
# 这种情况下需要指定排序规则，默认排序方法不会按价格排序
items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# 在这个例子中，我们要按价格排序

# 传统写法：
# def sort_items_price(index):
#     return index[1]
# 如果每个元素是元组，这里返回元组的第二个元素（价格）

# items.sort(key=sort_items_price)
# print(items)

# 使用 lambda（匿名函数）可以更简洁地定义一次性使用的函数作为参数
items.sort(key=lambda index: index[1])  # lambda 参数列表 : 表达式
print(items)
