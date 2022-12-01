for i in range(int(input())):
    count = 0
    for num_count in range(int(input())):
        a, b = map(int, input().split())
        while a % b != 0:
            a, b = b, a % b
        if b == 1:
            count += 1
    print(count)
