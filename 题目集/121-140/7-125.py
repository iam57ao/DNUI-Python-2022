num_list = []
for num in range(1000, 10000):
    if len(set(str(num))) == 4 and num % 11 == 0:
        num_sum = sum(map(int, list(str(num))))
        if num_sum == 6:
            num_list.append(num)
print(len(num_list), sorted(num_list), sep='\n')