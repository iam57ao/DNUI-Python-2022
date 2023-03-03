num = int(input())
num_list = []
while True:
    if num == 1:
        break
    elif num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    num_list.append(num)
print(",".join(list(map(str, num_list))))