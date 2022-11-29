dict1, dict2 = eval(input()), eval(input())
dict_out = dict1
for element in dict2:
    dict_out[element] = dict_out.get(element, 0) + dict2[element]
print(dict(sorted(dict_out.items())))