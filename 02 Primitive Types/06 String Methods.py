# 06 String Methods
course_name_python = "  python programming for beginners    "
# String method to convert to upper case
print(course_name_python.upper())
# String method to convert to lower case
print(course_name_python.lower())
# String method to convert to upper case first letter of each word
print(course_name_python.title())
# String method to remove blank spaces at the end and at the beginning of a string
print(course_name_python.strip())
# String method to remove blank spaces at the beginning of a string
print(course_name_python.lstrip())
# String method to remove blanck spaces at the end of a string
print(course_name_python.rstrip())
# String method to find index
print(course_name_python.find("gram"))
# String method to replace letter
print(course_name_python.replace("p", "P"))
# String method to check the existence of a caracter or a sequence of caracters, returns a boolean value
print("pro" in course_name_python)
print("abc" in course_name_python)
# String method to check if a sting does not contain a caracter or a sequence of caracters, returns a boolean value
print("pro" not in course_name_python)
print("abc" not in course_name_python)

# 字符串函数
# course.(出来的列表都是函数又叫方法)  python里所有东西都是对象  在对象中的函数叫做方法，可以通过点操作符访问，
# 1.upper 字符串全部转为大写
# 2.lower 字符串全部转为小写
# 3.title 字符串第一个字符大写
# 4.strip 删除字符串开头和结尾的所有空格
# 5.find 给定字符串的所在的序号
# 6.replace 用一个字符组合替代另一个字符组合
# 7.in 检测目标字符串中是否有某个字符组合("XXX" in course)
# 8.not 检查是否不含某个字符组合（也就是反转布尔值）
