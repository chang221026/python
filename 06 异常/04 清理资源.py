# 04 清理资源

# 有时候我们需要使用外部资源，比如文件、数据库、网络连接等。
# 每当我们使用这些资源后，完成任务时都需要释放它们。
# 例如，当我们打开一个文件时，应该在使用完毕后将其关闭。

try:
    file = open("04 Cleaning Up.py") # 这里我们打开一个文件，并将其存储在变量 file 中。
    age = int(input("Age: "))
    xfactor = 10 / age
#    file.close() # 这里我们关闭文件。但如果第 8 行或第 9 行发生异常，这行代码将不会执行。
except (ValueError, ZeroDivisionError):
    print("You did no enter a valid age.")
else: 
    print('No exceptions where thrown')
finally: # finally 块无论是否发生异常都会执行。
    file.close() # 在这里释放资源是更好的做法。


print("Executions continues")
