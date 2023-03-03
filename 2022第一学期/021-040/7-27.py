a = input()
print(len(a) == 18 and a[:17].isdigit() and (a[-1:] == "X" or a[-1:].isdigit()))
