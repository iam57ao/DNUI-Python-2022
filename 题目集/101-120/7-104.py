from sys import stdin
line_list = stdin.readlines()
output_list = []
for line in line_list:
    num_count, *num_list = list(map(int, line.split()))
    result = 1
    for element in num_list:
        if element % 2 != 0:
            result *= element
    output_list.append(result)
for output in output_list:
    print(output)
