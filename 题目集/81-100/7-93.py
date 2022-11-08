num = int(input())
i = 1
j = 1
while True:
    if j >= num:
        break
    print(str(j).rjust(5, " "), end="")
    i += 1
    if (i - 1) % 6 == 0:
        print()
    j = int((1 / (5 ** 0.5)) * (((1 + 5 ** 0.5) / 2) ** i - ((1 - 5 ** 0.5) / 2) ** i))
