num = int(input())
for i in range(num):
    if i == 0 or i == num - 1:
        print(num * str(num))
    else:
        print(f"{num}{'*' * (num - 2)}{num}")
