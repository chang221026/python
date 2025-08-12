# 05 格式化字符串

# 常见字符串操作
# https://docs.python.org/3/library/string.html#formatexamples

first_name = "Jose Miguel"
last_name = "Hargreaves Pimenta"
full_name = first_name + " " + last_name
print(full_name)
full_name_formated = f"{first_name} {last_name}"
print(full_name_formated)

# 格式化字符串 f"{xxx} {xxx}"    ==   xxx + " " + xxx