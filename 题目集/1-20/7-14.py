num = int(input())
print((num // 100) ** 3 + (num % 100 // 10) ** 3 + (num % 100 % 10) ** 3 == num)
