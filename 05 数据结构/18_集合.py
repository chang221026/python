# 18 集合（Set）

# Python 也有集合（set）这种数据类型。
# 集合是一个无序且不包含重复元素的容器。
# 基本用途包括成员检测、去重等。
# 集合还支持数学运算，如并集、交集、差集和对称差集。
# 可以使用大括号 {} 或 set() 创建集合。
# 注意：要创建一个空集合必须使用 set()，因为 {} 创建的是空字典。

numbers = [1, 1, 2, 5, 4, 5, 1, 2, 2, 1, 4, 5, 5]
uniques = set(numbers) # 去重
print(uniques)

# 集合支持和列表相似的方法
uniques.add(6)
print(uniques)

uniques.remove(6)
print(uniques)

print(len(uniques)) # 集合长度


# 集合最强大之处在于支持数学运算
first_set = {1, 2, 3, 4, 5}
second_set = {1, 2, 7, 8, 9}

print(first_set | second_set) # 并集
print(first_set.union(second_set)) # 同上
print(first_set & second_set) # 交集
print(first_set.intersection(second_set)) # 同上

print(first_set - second_set) # 差集（在 first_set 中但不在 second_set 中）
print(first_set.difference(second_set)) # 同上

print(second_set - first_set) # 差集（在 second_set 中但不在 first_set 中）
print(second_set.difference(first_set)) # 同上

print(first_set ^ second_set) # 对称差集（在两个集合中，但不同时存在）
print(first_set.symmetric_difference(second_set)) # 同上

# 使用集合：1.进行交并集运算 2.检测集合中是否包含一个元素 
# 集合是一种不排序的唯一性元素组合，集合里没有重复项，也不能排序，不能通过序号访问集合元素
