num = int(input())
num_str = str(num)
for i in range(num):
    if i == 0 or i == num - 1:
        print(num_str * num)
    else:
        print(num_str + " " * (num - 2) + num_str)
