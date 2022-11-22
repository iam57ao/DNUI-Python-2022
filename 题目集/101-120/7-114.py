for count in range(int(input())):
    stu_count = int(input())
    stu_list = []
    for i in range(stu_count):
        stu_list.append(input().split())
    out_list = sorted(stu_list, key=lambda stu: (- int(stu[1]), - int(stu[2]), stu[0]))
    rank = 0
    for index in range(len(out_list)):
        value = out_list[index]
        if index == 0 or out_list[index][1] != out_list[index - 1][1] or out_list[index][2] != out_list[index - 1][2]:
            rank = index + 1
        print(rank, *value)
