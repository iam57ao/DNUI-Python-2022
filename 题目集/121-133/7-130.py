for count in range(int(input())):
    a, b = input().split()
    num_add = int(a[::-1]) + int(b[::-1])
    print(int(str(num_add)[::-1]))