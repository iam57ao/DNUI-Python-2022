from sys import stdin
line_list = stdin.readlines()
for line in line_list:
    a, b = map(int, line.split())
    num_list = []
    for num in range(a, b + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            num_list.append(num)
    print(*num_list)
