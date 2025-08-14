# 22 解包操作符

numbers = [1, 2, 3]
print(numbers)
print(*numbers) # 使用 * 运算符，我们正在解包列表并将其作为单个元素传递给 print 函数。


values = list((range(10)))
print(values)
values  = [*range(10)] # 通过这个操作符，我们可以解包任何可迭代对象。
print(values)

my_text = [*"Hello Miguel"]
print(my_text)

# 我们可以将多个列表合并。
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
combined_lists = [*list_1, *list_2]
print(combined_lists)


# 我们也可以解包字典，但必须使用**

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 4, "c": 6}
combined_dict = {**dict_1, **dict_2} # 如果我们有多个具有相同键的值，将使用最后一个值。
print(combined_dict)

