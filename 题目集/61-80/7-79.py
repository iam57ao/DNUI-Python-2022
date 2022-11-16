sum_list = []
for count in range(int(input())):
    a, *b = map(int, input().split())
    sum_list.append(sum(b))
for sum_value in sum_list:
    if sum_value % 3 == 0 and sum_value % 5 == 0 and sum_value % 7 == 0:
        print("YES")
    else:
        print("NO")
