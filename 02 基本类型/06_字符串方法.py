# 06 字符串方法
course_name_python = "  python programming for beginners    "
# 将字符串转换为大写
print(course_name_python.upper())
# 将字符串转换为小写
print(course_name_python.lower())
# 将字符串中每个单词的首字母转换为大写
print(course_name_python.title())
# 去除字符串开头和结尾的空格
print(course_name_python.strip())
# 去除字符串开头的空格
print(course_name_python.lstrip())
# 去除字符串结尾的空格
print(course_name_python.rstrip())
# 查找子字符串的索引位置
print(course_name_python.find("gram"))
# 替换字符
print(course_name_python.replace("p", "P"))
# 检查字符串中是否存在某个字符或字符序列，返回布尔值
print("pro" in course_name_python)
print("abc" in course_name_python)
# 检查字符串中是否不存在某个字符或字符序列，返回布尔值
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
