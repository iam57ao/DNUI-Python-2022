from sys import stdin
num_list = stdin.readlines()
for num_line in num_list:
    print(sum(map(int, num_line.strip().split())))