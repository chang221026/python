# 09 Type Conversion
x = input("x: ")  # Even if the input is a number it will be read as a string
print(type(x))

y = int(x) + 5
print(f"x: {x} ; y: {y}")

# type converters
# int() converts to an interger

# float() converts to float

# bool() converts to boolean
# Falsy values - values that retunr False
print(bool(""))  # Double quotations returns False
print(bool(0))  # 0 returns False
print(bool(None))
# Other values return True
print(bool(2))
# str() converts to string



# int float bool str   bool(x)特殊，有类真类假概念，这些类真假值不是True或False,但是他们在编译时会被看成对应值
# 空字符串(布尔假) 数字0(布尔假)   None(布尔假)



# 使用input得到用户输入
# type 返回传入对象类型
