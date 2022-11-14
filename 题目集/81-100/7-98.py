import math


def factorial(num):
    if num == 0:
        return 1
    for element in range(1, num):
        num *= element
    return num


a = eval(input())
i = 1
count = 1
count_2 = 1
while True:
    if factorial(i) / count_2 <= a:
        break
    count_2 *= 2 * i + 1
    count += factorial(i) / count_2
    i += 1
print(round(count * 2, 5))

