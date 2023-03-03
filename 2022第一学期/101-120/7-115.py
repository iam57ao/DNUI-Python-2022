from sys import stdin
length = int(input())
line_list = stdin.readlines()
status = False
for line in line_list:
    x_list = line.split()
    x_max_num = max(map(int, x_list))
    for x_index in range(length):
        if int(x_list[x_index]) == x_max_num:
            y_list = [y.split()[x_index] for y in line_list]
            y_min_num = min(map(int, y_list))
            for y_index in range(length):
                if int(y_list[y_index]) == y_min_num and y_index == line_list.index(line):
                    print(y_index, x_index)
                    status = True
                    break
if not status:
    print("NONE")