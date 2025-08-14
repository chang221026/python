# 21 生成器表达式（Generator Expressions）

# 生成器表达式是一种简洁的生成器写法，用小括号括起来：
# generator_expression ::=  "(" expression comp_for ")"
# 它会返回一个新的生成器对象。
# 语法和推导式（列表推导式、字典推导式、集合推导式）相同，
# 只是用小括号 () 包裹，而不是中括号 [] 或大括号 {}。

# 与列表不同，生成器不会一次性把所有值存储到内存中，
# 而是每次迭代时动态生成一个值，因此更节省内存。

from sys import getsizeof # 导入 getsizeof 函数

values = (x * 2 for x in range(100))
print(values) # 打印生成器对象

for x in values:
    print(x)

print(getsizeof(values)) # 显示占用的内存字节数

