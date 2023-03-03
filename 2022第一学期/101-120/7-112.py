user_password = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}
for count in range(4):
    user, password = input(), input()
    try:
        if user_password[user] == password:
            print("登录成功")
            break
    except KeyError:
        print("登录失败")
        continue
    print("登录失败")
    continue
