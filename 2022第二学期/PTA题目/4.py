m, n = map(int, input().split())
lst1 = sorted(list(set(map(int, input().split()))))
lst2 = sorted(list(set(map(int, input().split()))))
lst1_index = lst2_index = 0
while lst1_index < len(lst1) and lst2_index < len(lst2):
    if lst1[lst1_index] == lst2[lst2_index]:
        print(lst1[lst1_index], end=' ')
        lst1_index += 1
        lst2_index += 1
        continue
    if lst1[lst1_index] < lst2[lst2_index]:
        lst1_index += 1
    else:
        lst2_index += 1
