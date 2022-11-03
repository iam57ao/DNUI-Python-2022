money_list = []
change_tup = (10, 5, 1)
for input_num in range(int(input())):
    money_list.append(int(input()))
for money in money_list:
    money_num = money
    change_dict = {10: 0, 5: 0, 1: 0 }
    for change in change_tup:
        change_dict[change] = money_num // change
        money_num %= change
    print(f"{money} = {change_dict[10]}*10 + {change_dict[5]}*5 + {change_dict[1]}*1")
