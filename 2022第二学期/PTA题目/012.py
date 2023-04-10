lst_s = []
lst_h = []
num = int(input())
data = input()
result = ""
if 2 <= num <= 10:
    for i in data:
        lst_s.append(i) if i == "S" else lst_h.append(i)
    while len(lst_s) != 0 and len(lst_h) != 0:
        result += lst_h.pop()
        result += lst_s.pop()
    for j in lst_s if lst_s else lst_h:
        result += j
    print(result)

else:
    print("ERROR")
