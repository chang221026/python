# 17 数组（Array）

# 当处理非常大的数字序列（如 10,000 个以上）时，数组在内存性能上更优。
# 只有在遇到性能问题时才考虑使用数组，否则建议使用列表或元组。

from array import array
# array 模块定义了一种对象类型，可以紧凑地表示基本值的数组：字符、整数、浮点数等。
# 数组与列表类似，但存储的对象类型是受限制的。
# 类型在创建数组对象时通过类型码（单个字符）指定，例如：
# "i" 表示有符号整数，"f" 表示浮点数等。
# https://docs.python.org/3/library/array.html

numbers = array("i", [1,2,3])
print(numbers)
