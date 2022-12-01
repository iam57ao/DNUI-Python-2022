for count in range(int(input())):
    num_count, *nums = map(int, input().split())
    odd_list, even_list = [], []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    odd_list, even_list = sorted(odd_list), sorted(even_list)
    odd_list.extend(even_list)
    print(*odd_list)