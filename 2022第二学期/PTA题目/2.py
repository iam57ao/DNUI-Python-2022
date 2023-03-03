for i in range(int(input())):
    lst1 = []
    lst2 = []
    lst1_index = lst2_index = 0
    out = []
    for j in range(int(input())):
        value = list(map(int, input().split()))
        lst1.extend([value[1], value[0]])
    for k in range(int(input())):
        value = list(map(int, input().split()))
        lst2.extend([value[1], value[0]])
    len1 = len(lst1)
    len2 = len(lst2)
    while lst1_index < len1 and lst2_index < len2:
        if lst1[lst1_index + 1] < lst2[lst2_index + 1]:
            if lst1[lst1_index] == 0:
                lst1_index += 2
                continue
            out.append(f"{f'+{lst1[lst1_index]}' if lst1[lst1_index] > 0 else f'{lst1[lst1_index]}'}x^{lst1[lst1_index + 1]}")
            lst1_index += 2
        elif lst1[lst1_index + 1] > lst2[lst2_index + 1]:
            if lst2[lst2_index] == 0:
                lst2_index += 2
                continue
            out.append(f"{f'+{lst2[lst2_index]}' if lst2[lst2_index] > 0 else f'{lst2[lst2_index]}'}x^{lst2[lst2_index + 1]}")
            lst2_index += 2
        else:
            if lst1[lst1_index] + lst2[lst2_index] == 0:
                lst1_index += 2
                lst2_index += 2
                continue
            out.append(f"{f'+{lst1[lst1_index] + lst2[lst2_index]}' if lst1[lst1_index] + lst2[lst2_index] > 0 else f'{lst1[lst1_index] + lst2[lst2_index]}'}x^{lst1[lst1_index + 1]}")
            lst1_index += 2
            lst2_index += 2
    odd_lst = (lst1 := lst1[lst1_index:]) if lst1_index < lst2_index else (lst2 := lst2[lst2_index:])
    for l in range(0, len(odd_lst), 2):
        if odd_lst[l] == 0:
            continue
        out.append(f"{f'+{odd_lst[l]}' if odd_lst[l] > 0 else f'{odd_lst[l]}'}x^{odd_lst[l + 1]}")
    print("".join(out)[1:])