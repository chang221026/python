# 07 抛出异常的成本

# 异常是有性能成本的

from timeit import timeit  # 从 "timeit" 模块中导入 "timeit" 函数，可以用来计算一段 Python 代码的执行时间。

code_1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

code_2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code_3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 /age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Code 1 execution time: ", timeit(code_1, number=10000)) # 1.9712759
print("Code 2 execution time: ", timeit(code_2, number=10000)) # 0.005862399999999823
print("Code 3 execution time: ", timeit(code_3, number=10000)) # 0.0021092000000000333

# 从执行时间可以看出，"code_3" 的运行速度最快，因为它没有抛出异常。
