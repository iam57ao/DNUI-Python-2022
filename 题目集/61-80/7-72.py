def isfloat(x):
    x = str(x)
    if x.count(".") == 1 and x.replace(".", "").isdecimal:
        return True
    else:
        return False


num_len = int(input())
if num_len == 0:
    print("除0错误，n不能等0\n程序结束")
else:
    num_list = []
    for i in range(num_len):
        num = input()
        if num.isdecimal() or isfloat(num):
            num = eval(num)
            num_list.append(num)
        else:
            break
    if len(num_list) != 0 and num_len == len(num_list):
        print(f"正确\navg={sum(num_list) / num_len:.2f}\n程序结束")
    else:
        print("数值错误\n程序结束")
