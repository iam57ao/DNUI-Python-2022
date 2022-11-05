sum_list = []
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        sum_list.append(a + b)
for sum_value in sum_list:
    print(sum_value)
    