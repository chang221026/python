# 06 *args

# def multiply(x, y):  # 这个函数只接受两个参数 x 和 y
#   return x * y

# multiply(2, 3)

def multiply(*numbers):  # 在参数前加 * 可以传入多个参数，这些参数会被组合成一个元组
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(1, 3, 6, 2, 8))


# 如何向函数传递一组参数
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
