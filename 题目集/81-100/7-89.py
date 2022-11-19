num_list = []
for num in range(2, int(input())):
    sum_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_list.append(i)
    if sum(sum_list) == num:
        num_list.append(num)
print(*num_list, sep=",")
