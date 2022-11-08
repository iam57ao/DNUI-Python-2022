num = int(input())
for i in range(0, num):
    if i < (num / 2) - 1:
        print(("*" * (2 * (i + 1) - 1)).rjust(int((num + 1) / 2 + (i + 1)), " "))
    elif i > (num / 2) - 1:
        print(("*" * (2 * (num - i) - 1)).rjust(int((num + 1) / 2 + (num - i)), " "))
    else:
        print(("*" * num).rjust(num + 1, " "))