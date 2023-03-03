len1, *lst1 = list(map(int, input().split()))
len2, *lst2 = list(map(int, input().split()))
lst1_max_index = len1 * 2 - 1
lst2_max_index = len2 * 2 - 1
lst1_index = lst2_index = 0
lst_out = []
sum_all = 0
while lst1_index <= lst1_max_index and lst2_index <= lst2_max_index:
    if lst1[lst1_index + 1] > lst2[lst2_index + 1]:
        if lst1[lst1_index] == 0:
            lst1_index += 2
            continue
        lst_out.extend([lst1[lst1_index], lst1[lst1_index + 1]])
        sum_all += pow(lst1[lst1_index], lst1[lst1_index + 1])
        lst1_index += 2
    elif lst1[lst1_index + 1] < lst2[lst2_index + 1]:
        if lst2[lst2_index] == 0:
            lst2_index += 2
            continue
        lst_out.extend([lst2[lst2_index], lst2[lst2_index + 1]])
        sum_all += pow(lst2[lst2_index], lst2[lst2_index + 1])
        lst2_index += 2
    else:
        if lst1[lst1_index] + lst2[lst2_index] == 0:
            lst1_index += 2
            lst2_index += 2
            continue
        lst_out.extend([lst1[lst1_index] + lst2[lst2_index], lst1[lst1_index + 1]])
        sum_all += pow(lst1[lst1_index] + lst2[lst2_index], lst1[lst1_index + 1])
        lst1_index += 2
        lst2_index += 2
odd_lst = (lst1 := lst1[lst1_index:]) if len1 > len2 else (lst2 := lst2[lst2_index:])
for i in range(0, len(odd_lst), 2):
    if odd_lst[i] == 0:
        continue
    lst_out.extend([odd_lst[i], odd_lst[i + 1]])
    sum_all += pow(odd_lst[i], odd_lst[i + 1])
print(" ".join(list(map(str, lst_out))) if sum_all != 0 else "0 0")
