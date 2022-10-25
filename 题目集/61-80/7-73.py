value = input()
index = input()
if index.isdecimal() or index.count("-") == 1 and index.replace("-", "").isdecimal:
    index = int(index)
    if 0 <= index <= len(value) - 1 or -len(value) < index < 0:
        print(value[index])
    else:
        print("输入下标有误")
else:
    print("输入下标有误")
