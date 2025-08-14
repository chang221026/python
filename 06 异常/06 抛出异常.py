# 06 抛出异常

# 我们也可以在自己的代码中抛出异常

def calculate_xfactor(age): # 如果传入的参数是 0 或更小，这个函数会抛出异常
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age # 年龄不能为零或更小
# calculate_xfactor(-1)

# 如果我们运行这个程序，它会崩溃，并且得到如下错误：

# File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\06 Raising Exceptions.py", line 10, in <module>
#     calculate_xfactor(-1)
#   File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\06 Raising Exceptions.py", line 7, in calculate_xfactor
#     raise ValueError("Age can not be zero or less")
# ValueError: 年龄不能为零或更小

# 这是因为我们没有正确地处理异常，也就是没有使用 "try:" 块。

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# 抛出异常并不推荐，因为它的开销比较大