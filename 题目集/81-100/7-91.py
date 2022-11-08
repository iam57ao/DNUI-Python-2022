num_input = input().split()
m, n = sorted(list(map(int, num_input)))

num_list = []
i, j = 1, 1
for element in range(1, m + 1):
    if m % element == 0 and n % element == 0:
        num_list.append(element)
        m, n = m // element, n // element
num_list.extend([m, n])
for element in num_list[:-2]:
    i *= element
j = i
for element in num_list[-2:]:
    j *= element
print(i, j)