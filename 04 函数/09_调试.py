# 09 调试

def multiply(*numbers):  # 在参数前加 * 可以传入多个参数，这些参数会被组合成一个元组
    total = 1
    for number in numbers:
        total = total * number
        return total  # 将这个 return 语句缩进到 for 循环内部，是在模拟一个 bug


print("开始")
print(multiply(1, 2, 3))



# debug  第一次找到左侧debug,点最上面设置图标，出现launch.json文件，文件里面是debug的设置
# 1.F9 断点
# 2.F5 执行代码直到中断这行
# 3.F10 每执行一步
# 4.F11 进入函数内部
# 5.shift + F5  终止debug
# 6.shift + F11 知道一个函数是正确的，直接跳出




# win快捷键
# 1. End 移到行末
# 2. Home 移到行首
# 3. ctrl + home 移到文件最开始
# 4. ctrl + end 移到文件最结尾
# 5. alt + ↑/↓ 把这一行向上向下移动
# 6. shift alt ↑/↓ 复制一行或几行
# 7. Ctrl /  注释
# 8. mul  mtl   都可以敲出multiply


# Mac快捷键
# 1. fn → 移到行末
# 2. fn ← 移到行首
# 3. fn ↑ 移到最开始
# 4. fn ↓ 移到最末尾
# 5. alt/option ↑/↓ 光标当前行上下移动
# 6. cmd / 注释