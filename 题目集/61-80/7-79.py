num_list = []
for line in range(int(input())):
    a, *b = map(int, input().split())
    num_list.append(sum(b))
for num in num_list:
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print("YES")
    else:
        print("NO")
        