money_list = []
for count in range(int(input())):
    money_list.append(int(input()))
for money in money_list:
    print(f"{money} = {money // 10}*10 + {money % 10 // 5}*5 + {money % 10 % 5}*1")
