# 20 字典推导式（Dictionary Comprehensions）

# 字典推导式可以通过任意的键和值表达式来创建字典。
# 此外，字典推导式可用于从任意键值表达式创建字典：
# {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

# 当键是简单的字符串时，有时使用关键字参数来指定键值对会更为方便：
# dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

valores = {x: x * 2 for x in range(5)}
print(valores)