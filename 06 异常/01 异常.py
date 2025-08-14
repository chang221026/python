# 01 异常

# 在程序运行过程中检测到的错误称为异常。

# 错误和异常
# https://docs.python.org/3/tutorial/errors.html

# 内置异常
# https://docs.python.org/3/library/exceptions.html

numbers = [1, 2]
print(number[3])

# 运行这个程序会报错，因为列表中没有索引 3
# File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\01 Exceptions.py", line 10, in <module>
#     print(numnbers[3])
# IndexError: list index out of range（索引错误：列表索引超出范围）

age = int(input("Age: "))

# 如果输入一个非数字的值，这段代码会报错
# File "c:/Users/jmigu/iCloudDrive/Os meus documentos/Educação/Code with Mosh/The Complete Python Course/HelloWorld/06 Exceptions (20m)/01 Exceptions.py", line 17, in <module>
#     age = int(input("Age: "))
# ValueError: invalid literal for int() with base 10: 'a'
# （值错误：无法将 'a' 转换为十进制整数）
