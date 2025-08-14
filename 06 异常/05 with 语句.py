# 05 with 语句

# 我们有一种更简洁、更清晰的方法，可以实现和 finally 块相同的效果。
# 但它只适用于某些对象。

try:
    with open("05 The With Statement.py") as file:  # 这里我们使用 with 语句打开文件，并将其存储在变量 file 中。
        print('File open')  # 当我们用 with 语句打开文件时，无论是否有 finally 块，Python 都会自动关闭文件。
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("你输入的年龄无效。")
else: 
    print('没有抛出任何异常')

# 如果一个对象有这两个方法，我们就说该对象支持上下文管理协议（context management protocol）。
# 这样我们就可以用 with 语句来管理它，Python 会自动调用 exit 方法并释放外部资源。
# file.__enter__
# file.__exit__

# 有时我们可能会同时操作多个文件
# with open("05 The With Statement.py") as file, open("04 Cleaning Up.py") as file2:
