# 03 三元运算符

age1 = 17
if age1 >= 18:
    print("符合条件")
else:
    print("不符合条件")

# 有一种更简洁的方式可以写出相同的逻辑，并得到相同的结果
age2 = 20
message = "符合条件" if age2 >= 18 else "不符合条件"
print(message)
