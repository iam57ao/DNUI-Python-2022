def gcd(a, b):
    value = a * b
    while a % b != 0:
        a, b = b, a % b
    return value // b


for i in range(int(input())):
    input_list = list(map(int, input().split()))
    num_list = input_list[3:]
    num = gcd(*input_list[1:3])
    while num_list:
        num = gcd(num, num_list.pop())
    print(num)