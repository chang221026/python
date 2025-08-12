# 05 默认参数

# 函数中的所有参数默认都是必需的，在本节中我们将把一个参数设为可选参数。
# 所有可选参数必须放在必需参数之后。

def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 6))



# 当缺少第二个参数，但是默认传参第二个等于1，所以传入第一个参数不传入第二个，第二个就默认为我们特别声明的值

# 所有可选参数都应该在必要参数后面。 increment(number, by=1, letter) 这样是错的，应该increment(number, letter, by=1)