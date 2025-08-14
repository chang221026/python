# 04 遍历列表/列表循环

letters = ["a", "b", "c", "d"]

# 直接遍历列表，得到的是每个元素的值
for letter in letters:
    print(letter)

# 如果想同时获取每个元素的索引，可以使用内置函数 enumerate()
for letter in enumerate(letters):
    print(letter)
# 返回的是一个元组 (索引, 元素)

# 使用解包，可以同时得到索引和值
for index, letter in enumerate(letters):
    print(index, letter)
