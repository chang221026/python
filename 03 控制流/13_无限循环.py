# 13 无限循环

while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break
