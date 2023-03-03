num = input()
if not num.isdecimal():
    print("值错误，您必须输入数值")
else:
    if int(num) == 0:
        print("算术错误，您不能输入0")
    else:
        print(f"20除以{num}的结果是: {20 / int(num):.2f}\n没有出现异常")
