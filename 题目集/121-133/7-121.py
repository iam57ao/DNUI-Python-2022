for count in range(int(input())):
    m, n, *set_list = map(int, input().split())
    if set(set_list[:m]) - set(set_list[m:]):
        print(*(set(set_list[:m]) - set(set_list[m:])))
    else:
        print("NULL")
