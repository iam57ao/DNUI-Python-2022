lst1 = list(map(int, input().split()))[:-1]
lst2 = list(map(int, input().split()))[:-1]
lst1_length = len(lst1)
lst2_length = len(lst2)
lst1_index = lst2_index = 0
new_list = []
while lst1_index < lst1_length and lst2_index < lst2_length:
    if lst1[lst1_index] < lst2[lst2_index]:
        print(lst1[lst1_index], end=" ")
        lst1_index += 1
    elif lst1[lst1_index] > lst2[lst2_index]:
        print(lst2[lst2_index], end=" ")
        lst2_index += 1
    else:
        print(lst1[lst1_index], end=" ")
        print(lst2[lst2_index], end=" ")
        lst1_index += 1
        lst2_index += 1
odd_lst = (lst1 := lst1[lst1_index:]) if lst1_index < lst1_length else (lst2 := lst2[lst2_index:])
while odd_lst:
    print(odd_lst.pop(0), end=" ")
