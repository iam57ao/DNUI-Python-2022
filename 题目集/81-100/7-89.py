num_list = []
for num in range(2, int(input())):
    divisible_num = []
    for i in range(1, num):
        if num % i == 0:
            divisible_num.append(i)
    if sum(divisible_num) == num:
        num_list.append(num)
num_list = map(str, num_list)
print(",".join(num_list))
