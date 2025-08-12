# 04 关键字参数

# def increment(number, by):
#    return number + by

# result = increment(2, 1)
# print(result)

# 也可以这样使用
def increment(number, by):
    return number + by


print(increment(2, by=1))

# by=1 Its the keyword arguent, if a function as multiple arguments, the code can be more readable by using keyword arguments.
# by=1就是关键字传参，当有多个参数你不知道他们作什么的时候
