# 08 for 循环

# 用于重复执行某个任务
# 在这个例子中，我们尝试至少给用户发送 3 次消息

for number in range(3):  # range 生成 0, 1, 2
    print("尝试", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range 生成 1, 2, 3
    print("尝试", number, number * ".")

for number in range(1, 10, 2):  # range 生成 1, 3, 5, 7, 9
    print("尝试", number, number * ".")

# for number in range(1,10,2):   从 1 开始到 10（不包含 10），步长为 2
