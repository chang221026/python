# 07 列表排序

numbers = [5, 51, 2, 15, 6]
print(numbers)

# 使用 sort() 方法对列表进行排序（默认升序）
numbers.sort()
print(numbers)

# 传入 reverse=True 参数实现降序排序
numbers.sort(reverse=True)
print(numbers)

# # sorted() 函数会返回一个新的排序后的列表，不会修改原列表
print(sorted(numbers))
print(sorted(numbers, reverse=True))


# 复杂对象的列表，例如元组列表（每个订单包含商品名和价格）
# 这种情况下，需要定义一个函数指定排序规则，直接用 sort() 或 sorted() 不会按预期工作
items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# 在这个例子中，我们要按价格排序


def sort_items_price(index):
    return index[1]
# 如果每个元素是元组，这里返回元组的第二个元素（价格）


items.sort(key=sort_items_price) # 没有调用函数，只是传入函数的引用
print(items)
