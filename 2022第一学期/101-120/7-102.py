line_list = []
for count in range(int(input())):
    line_list.append(input())
for element in line_list:
    try:
        end = eval(element)
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except SyntaxError:
        print("SyntaxError")
    else:
        print(f"{end:.2f}")