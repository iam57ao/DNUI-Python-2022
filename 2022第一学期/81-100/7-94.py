num = int(input())
ls = []
i = 2
while i <= num:
    if num % i == 0:
        ls.append(i)
        num = num // i
    else:
        i += 1
print(*ls, "")
