# 02 访问列表元素

#  a   b   c   d - 列表示例
#  0   1   2   3 - 每个元素的正向索引位置
# -4  -3  -2  -1 - 每个元素的反向索引位置
letters = ["a", "b", "c", "d"]
print(letters)

first_item = letters[0]  # 访问列表中索引为 0 的元素
print(first_item)

letters[0] = "A"  # 修改列表中第一个元素
print(letters)

numbers = list(range(20))
print(numbers)

# 类似字符串，可以对列表进行切片 [起始索引 : 结束索引 : 步长]，所有参数都是可选的
numbers_slice = numbers[2:15:2]
print(numbers_slice)

# 使用切片可以反转列表
numbers_revers = numbers[::-1]
print(numbers_revers)
