# 03 构造函数

# 当创建一个 Point 对象时，如果我们想提供 x, y, z 坐标，
# 为了实现这个功能，我们需要一个构造函数（constructor），它是一个在创建新 Point 对象时会被自动调用的特殊方法。
class Point:
    def __init__(self, x, y, z): # 要创建构造函数，我们调用特殊方法 "__init__"。self 是对当前对象的引用，所以我们用 self 来设置属性
        self.x = x # x, y, z 是 Point 对象的属性
        self.y = y
        self.z = z

    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")


point = Point(100, 200, 10)
print(point.x)
point.draw() # 当调用 ".draw" 方法时，我们不需要传递参数，因为 Python 会自动传递当前对象
