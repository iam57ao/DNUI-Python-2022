import math


def factorial(num):
    if num == 0:
        return 1
    for element in range(1, num):
        num *= element
    return num


num = float(input())
e = 1
count = 1
while math.e - e > num:
    e += 1 / factorial(count)
    count += 1
print(e + 1 / factorial(count))