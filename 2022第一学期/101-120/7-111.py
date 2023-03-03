str_dict = {}
while True:
    str_input = input()
    if str_input == "q":
        break
    str_dict[str_input] = str_dict.get(str_input, 0) + 1
sorted_dict = sorted(str_dict.items(), key=lambda x: x[1])
print(*sorted_dict[-1])