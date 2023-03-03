from sys import stdin
num_list = map(int, stdin.read().split())
for num in num_list:
    for i in range(1, 2 * num):
        if i <= num:
            print(("*" * (2 * num - (2 * i - 1))).rjust(2 * num - i, " "))
        else:
            print(("*" * (2 * num - (2 * (num - i + num) - 1))).rjust(2 * num - (num - i + num), " "))