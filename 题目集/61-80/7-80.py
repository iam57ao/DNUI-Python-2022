from sys import stdin
line_list = stdin.readlines()
for line in line_list:
    a, b = map(int, line.split())
    print(a + b)