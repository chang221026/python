# 12 while 循环

number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
