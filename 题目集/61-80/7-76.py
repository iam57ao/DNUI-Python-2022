num_list = [2]
for num in range(3, 5000):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        num_list.append(num)

state = False
num = int(input())
for i in num_list:
    if state:
        break
    for j in num_list:
        if i + j == num:
            print(f"{num} = {i} + {j}")
            state = True
            break
