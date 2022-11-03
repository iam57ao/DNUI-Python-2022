num = int(input())
if num > 2:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "no")
            break
    else:
        print(num, "yes")
elif num == 1:
    print(num, "no")
else:
    print(num, "yes")
