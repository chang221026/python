# 05 Default Arguments

# All the parameters that are in the function are required by default, in this lecture we are going make the a parameter optional.
# All the optinal parameters must come after the required parameter


def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 6))


# 当缺少第二个参数，但是默认传参第二个等于1，所以传入第一个参数不传入第二个，第二个就默认为我们特别声明的值

# 所有可选参数都应该在必要参数后面。 increment(number, by=1, letter) 这样是错的，应该increment(number, letter, by=1)