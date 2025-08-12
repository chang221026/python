# 07 **args

def save_user(**user):  # 保存用户信息的函数
    print(user)


# 这里我们向函数传递了 3 个关键字参数
save_user(id="V857093-N", name="Jose", age=36)
# {'id': 'V857093-N', 'name': 'Jose', 'age': 36}  这会返回一个字典（属于复杂对象）
