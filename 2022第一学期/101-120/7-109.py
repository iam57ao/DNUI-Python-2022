dict1, dict2 = eval(input()), eval(input())
dict_out = {}
for element1 in dict1:
    dict_out[element1] = dict1[element1]
for element2 in dict2:
    dict_out[element2] = dict_out.get(element2, 0) + dict2[element2]
output = dict(sorted(dict_out.items(), key=lambda x: x[0] if type(x[0]) is int else ord(str(x[0]))))
print(str(output).replace(" ", "").replace("'", '"'))