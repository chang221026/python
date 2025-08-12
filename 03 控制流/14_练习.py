# 11 练习

# 输出偶数（2 4 6 8），然后输出消息 "We have 4 even numbers"
# 2
# 4
# 6
# 8
# We have 4 even numbers

# 我的答案
for number_even in range(1, 10):
    if number_even % 2 == 0:
        print(number_even)
    elif number_even > 8:
        print("我们有 4 个偶数")
        break

# Mosh 的答案
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count = count + 1
        print(number)
print(f"我们有 {count} 个偶数")

# 在我的答案中，我没有统计偶数的数量
