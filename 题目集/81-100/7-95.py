def factorial(num):
    if num == 0:
        return 1
    for element in range(1, num):
        num *= element
    return num


num_input = int(input())
ls = []
for i in range(1, num_input + 1):
    if i % 2 == 0:
        continue
    ls.append(factorial(i))
print(f"sum={sum(ls)}")