# 01 列表

# 字符串列表示例
letters = ["a", "b", "c"]
print(letters)

# 整数列表示例
numbers = [1, 2, 3, 4]
print(numbers)

# 这个列表中的每个元素本身又是一个列表，这就创建了一个二维列表（矩阵）
matrix = [[0, 1], [2, 3]]
print(matrix)

# 创建列表的示例
zeros = [0] * 5
print(zeros)

# 拼接两个列表
combined = zeros + letters
print(combined)

# 创建一个从 5 到 20 的数字列表
list_range = list(range(5, 21))
print(list_range)

# 将字符串转换为列表
string_list = list("Python")
print(string_list)

# 检查列表中元素的数量
item_in_string_list = len(string_list)
print(item_in_string_list)




# 列表中元素可以是不同类型
# len获取列表中元素个数