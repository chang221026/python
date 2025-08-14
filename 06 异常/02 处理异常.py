# 02 Handling Exceptions

# 要处理异常，我们需要把语句放在 try 块中。
# 当 Python 遇到 try 块时，会执行其中的每一条语句；
# 如果其中任何一条语句抛出异常，那么 except 块中的代码就会被执行。
# 如果没有抛出异常，那么 except 块中的代码不会执行。

try: # try 块
    age = int(input("Age: "))
except ValueError as ex: # 在这里我们处理非数字输入时的 ValueError 异常。
    # "as ex" 表示把异常对象赋值给变量 ex，这样我们就可以获取异常的详细信息。
    print("You did no enter a valid age.")
    print(ex) # 打印异常信息
    print(type(ex)) # 打印异常的类型
else: #可以添加一个可选的 else 块。如果未发生任何异常，我们在此处添加的代码将会被执行。
    print('No exceptions where thrown')

print("Executions continues") # 因为我们正确处理了异常，程序会继续执行这一行，而不会崩溃
