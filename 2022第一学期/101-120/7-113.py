work_list = input().split()
work_count = {}
for work in work_list:
    work_count[work] = work_count.get(work, 0) + 1
work_count = sorted(work_count.items(), key=lambda count: -count[1])
for out in work_count:
    print(*out, sep=":")