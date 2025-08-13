# 03 列表解包

numbers = [1, 2, 3]
print(numbers)

# 将列表中的元素分别赋值给变量
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# 更好的方式是使用列表解包
first, second, third = numbers
print(first)
print(second)
print(third)
# 这和上面第 6、7、8 行代码是一样的，等号左侧变量的数量必须与列表中元素的数量相同。

# 如果我们有一个很长的列表，只想解包前两个元素，把剩下的元素放到另一个列表中
numbers_0_19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers_0_19)
first, second, *others = numbers_0_19
print(first)
print(second)
print(others)

# 例如，如果我们想解包第一个和最后一个元素，其余的放到中间
first, *others, last = numbers_0_19
print(first)
print(others)
print(last)