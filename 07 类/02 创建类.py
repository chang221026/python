# 02 创建类
class Point: # 命名类时我们使用帕斯卡命名法（Pascal Case），例如 "ClassName"，每个单词首字母大写且不使用下划线
    def draw(self): # 然后我们定义一个函数，按照惯例，类中的每个函数至少要有一个参数，我们把这个参数称为 self
        print("draw")


point = Point()
point.draw()
print(type((point))) 
# Prints <class '__main__.Point'> # __main__ 是我们模块的名字

print(isinstance(point, Point)) # 有时候我们有一个对象，想判断该对象是否是某个类的实例


  