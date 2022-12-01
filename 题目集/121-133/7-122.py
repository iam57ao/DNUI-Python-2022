input_str = input()
out_list = []
for element in input_str:
    if element not in out_list:
        out_list.append(element)
    if len(out_list) == 10:
        break
print(*out_list, sep='')
