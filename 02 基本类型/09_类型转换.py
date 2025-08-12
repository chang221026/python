# 09 类型转换
x = input("x: ")  # 即使输入的是数字，也会被读取为字符串
print(type(x))

y = int(x) + 5
print(f"x: {x} ; y: {y}")

# 类型转换函数
# int() 转换为整数

# float() 转换为浮点数

# bool() 转换为布尔值
# 假值（Falsy values）- 会返回 False 的值
print(bool(""))  # 空字符串返回 False
print(bool(0))  # 数字 0 返回 False
print(bool(None))  # None 返回 False
# 其他值会返回 True
print(bool(2))
# str() 转换为字符串





# int float bool str   bool(x)特殊，有类真类假概念，这些类真假值不是True或False,但是他们在编译时会被看成对应值
# 空字符串(布尔假) 数字0(布尔假)   None(布尔假)

# 使用input得到用户输入
# type 返回传入对象类型
