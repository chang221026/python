# 09 For..Else
# for else循环
# Lesson how to break a for loop

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")



