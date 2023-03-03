a, b = map(int, input().split())
value = a * b
while a % b != 0:
    a, b = b, a % b
print(b, value // b)