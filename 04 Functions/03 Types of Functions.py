# 03 Types of Functions

# 1 - Function that perform a task


def greet(name):
    print(f"Hi {name}")


greet("Miguel")


# 2 - Functions that return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Pimenta")
print(message)


# print(greet("mosh")) None是greet函数返回值，在python中所有函数默认返回一个None的对象，除非你特别设置一个其他的值



# 函数：可以执行一个任务 \ 函数计算并返回一些值


