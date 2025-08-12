# 12 Exercise

# 编写一个函数，接收一个整数作为输入并返回以下结果：
# 对于 3 的倍数，打印 "Fizz" 代替数字
# 对于 5 的倍数，打印 "Buzz" 代替数字
# 对于同时是 3 和 5 的倍数的数字，打印 "FizzBuzz" 代替数字


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 != 0):
        print("Fizz")
    elif (input % 3 != 0) and (input % 5 == 0):
        print("Buzz")
    elif (input % 3 == 0) and (input % 5 == 0):
        print("FizzBuzz")
    else:
        print(input)


fizz_buzz(7)


# Mosh anwser


def fizz_buzz_mosh(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 != 0):
        return "Fizz"
    elif (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz_mosh(15))
