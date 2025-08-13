# 12 zip 函数

# zip() 函数返回一个 zip 对象，可以将多个可迭代对象组合成元组
# 返回的结果是一个元组列表，第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素
# 如果传入的序列长度不一致，则返回的结果会截断为最短序列的长度

list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40, 50, 60]

combined_list = zip(list_1, list_2)
print(list(combined_list))

list_3 = list(zip("abc", list_2, list_1))
print(list_3)
