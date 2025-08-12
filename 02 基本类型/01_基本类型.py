# 01 变量 / 2 - 变量名 / 3 - 字符串

import math
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(students_count)
print(rating)
print(course_name)
print(len(course_name))
print(course_name[0])
print(course_name[-2])
print(course_name[0:5])

# 使用变量将数据保存在内存中，运行代码时，python编译器会给这个变量分配地址，这个变量名字就引用了那个地址。所以，变量名就像标签一样,我们可以在程序任何位置通过访问地址得到数据
# 整数 浮点数 布尔类型 字符串     布尔值只有False和True 其他形式均为错误
# 变量名 1.全小写 2.名字有意义 3.单词间用下划线_ 4.赋值符号两边加空格 
# 字符串"和'都可以，偏好用"，还有三引号，用来定义一个长字符串("""XXXXX""")
# 字符串知识点 1.获取字符串长度 len(course) 2.[]访问字符串中特定字符  3.冒号分割字符串    course[0]  course[-1]  course[0:3](开始:结束)  course[:](也是原本字符串)



# 函数（方法）用来处理特定任务的复用代码