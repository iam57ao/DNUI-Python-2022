length = int(input())
line_list = [list(map(int, input().split())) for line_count in range(length)]
count = 0
for y_index in range(length):
    x_max = max(line_list[y_index])
    for x_index in range(length):
        x = line_list[y_index][x_index]
        if x == x_max:
            y_list = [y[x_index] for y in line_list]
            y_min = min(y_list)
            if y_min == x:
                count += 1
print(count)