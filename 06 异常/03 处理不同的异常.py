# 03 处理不同类型的异常

try: # try block
    age = int(input("Age: "))
    xfactor = 10 / age # 如果 age 为 0（数值类型），这一行会产生 "ZeroDivisionError" 错误。我们不能用数字除以零
except (ValueError, ZeroDivisionError): # 比起单独再写一个异常处理块，把多个异常类型放在一个元组里更简洁。
    print("You did no enter a valid age.")
#except ZeroDivisionError: # 我们也可以单独添加一个异常处理块，或者将 "ZeroDivisionError" 放到上面的 except 块里。
#    print("Age can not be zero")
else: # 可选的 else 块。如果没有发生任何异常，这里的代码会被执行。
    print('No exceptions where thrown')

print("Executions continues") # 因为我们正确处理了异常，这一行会被执行，程序不会崩溃。

