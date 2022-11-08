m, n = map(int, input().split())
for num in range(m, n + 1):
    if num % 2 != 0:
        continue
    divisible_list = [1]
    for i in range(2, num // 2 + 1):
        if sum(divisible_list) <= num:
            if num % i == 0 and i not in divisible_list:
                divisible = num // i
                divisible_list.extend([i, divisible])
        else:
            break
    else:
        if sum(divisible_list) == num:
            print(f"{num} = {' + '.join(list(map(str, sorted(divisible_list))))}")
