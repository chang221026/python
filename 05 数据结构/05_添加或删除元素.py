# 05 添加或删除元素

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)

# 在列表末尾添加元素
letters.append("h")
print(letters)

# 使用 insert() 方法在指定位置添加元素
# 第一个参数是位置索引，第二个参数是要添加的元素
letters.insert(2, "-")
print(letters)

# 使用 pop() 方法删除元素
# 不传参数时，删除最后一个元素
letters.pop()
print(letters)

# 传入索引参数时，删除该位置的元素
letters.pop(2)
print(letters)

# 使用 remove() 方法删除指定值的元素
# 这里会删除列表中第一个 "c"
letters.remove("c")
print(letters)
# 如果有多个 "c"，需要遍历列表逐一删除

# 使用 del 语句删除元素
# 可以删除单个元素或通过切片删除一段范围的元素
del letters[0:2]
print(letters)

# 使用 clear() 方法清空列表，删除所有元素
letters.clear()
print(letters)
