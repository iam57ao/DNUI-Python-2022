mouth_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_count = 0
y, m, d = map(int, input().split("/"))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    mouth_day[1] = 29
    for i in range(m - 1):
        day_count += mouth_day[i]
    print(day_count + d)
else:
    for i in range(m - 1):
        day_count += mouth_day[i]
    print(day_count + d)
