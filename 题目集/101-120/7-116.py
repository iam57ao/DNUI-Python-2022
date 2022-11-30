def saddle_point(y_length, x_length):
    point_list = []
    line_list = [list(map(int, input().split())) for line_count in range(y_length)]
    for y_index in range(y_length):
        x_max = max(line_list[y_index])
        for x_index in range(x_length):
            x = line_list[y_index][x_index]
            if x == x_max:
                y_list = [y[x_index] for y in line_list]
                y_min = min(y_list)
                if y_min == x:
                    point_list.append(f"{x} {y_index} {x_index}")
    if point_list:
        return "\n".join(point_list)
    return "Not"


try:
    while True:
        print(saddle_point(*map(int, input().split())))
except EOFError:
    pass
