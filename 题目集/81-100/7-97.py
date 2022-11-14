num, count = map(int, input().split())
num_list = list(range(1, num + 1))
out_list = []
while len(num_list) != 0:
    if len(num_list) == 1:
        out_list.append(num_list.pop())
    elif len(num_list) <= count:
        out_list.append(num_list.pop(count % len(num_list) - 1))
        num_list = num_list[count % len(num_list) - 1:] + num_list[:count % len(num_list) - 1]
    else:
        out_list.append(num_list.pop(count - 1))
        num_list = num_list[count - 1:] + num_list[:count - 1]
print(*out_list)