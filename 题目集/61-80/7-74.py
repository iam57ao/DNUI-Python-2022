num = int(input())
if num != 1:
    for count in range(2, int(num ** 0.5) + 1):
        if num % count == 0:
            print(num, "no")
            break
    else:
        print(num, "yes")
else:
    print("1 no")