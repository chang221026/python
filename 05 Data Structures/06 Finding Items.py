# 06 查找元素

letters = ["a", "b", "c", "d", "e", "f", "g"]

# 使用 index() 方法查找指定元素的索引位置
print(letters.index("d"))
# 如果 index() 方法传入的元素在列表中不存在，会抛出错误
# 因此最好先检查该元素是否存在于列表中

# 示例 1
if "d" in letters:
    print(letters.index("d"))

# 示例 2
# 使用 count() 方法统计指定元素在列表中出现的次数
print(letters.count("g"))