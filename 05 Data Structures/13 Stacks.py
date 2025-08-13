# 13 栈（Stack）

# 栈是一种数据结构，像一摞书一样，最后放在最上面的书会最先被移走。
# LIFO：后进先出（Last In - First Out）

# 一个很好的例子是浏览器的“后退”功能


browsing_session = []
browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# browsing_session.append(4)
print(browsing_session)

browsing_session.pop()
print(browsing_session)

# browsing_session[-1]  # 获取栈顶元素
if not browsing_session:  # 如果栈为空，就无法再“后退”
    print("disable")
    