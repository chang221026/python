# 09 For..Else
# for..else 循环
# 学习如何在 for 循环中使用 break

successful = False
for number in range(3):
    print("尝试")
    if successful:
        print("成功")
        break
else:
    print("尝试了 3 次仍然失败")
