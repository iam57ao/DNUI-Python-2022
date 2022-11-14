def int_abs(x):
    return abs(int(x))


num_input = list(map(int_abs, input().split()))
i = 0
sum_list = []
for element in str(min(num_input))[::-1]:
    sum_list.append(int(str(max(num_input))[::-1][i]) * int(element))
    i += 1
print(sum(sum_list))