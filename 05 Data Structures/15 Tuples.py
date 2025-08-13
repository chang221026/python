# 15 元组（Tuple）

# 元组本质上是只读的列表，创建后不能修改

points = (1, 2, 3) # 用圆括号定义的是元组
print(type(points))

points_1 = (1, 2, 3, 4, 5) + (6, 7, 8, 9) # 元组拼接
print(points_1)

points_2 = (1, 2, 3, 4, 5) * 3 # 元组重复
print(points_2)

text_tuple = tuple("Hello World") # 字符串是可迭代对象，可以用 tuple() 转为元组
print(text_tuple)

# 元组可以用 list() 转为列表
print(list(points_1))

# 像列表一样可以通过索引访问元组元素
print(points[1])

# 元组解包
x, y, z = points
print(f"x: {x}\ny: {y}\nz: {z}")

# 检查元素是否在元组中
if 2 in points:
    print("Exists")
else:
    print("Not there")



# 用元组的条件： 处理一系列对象时，你想确保不会意外的编辑这个序列，不会添加或删除已有的对象。