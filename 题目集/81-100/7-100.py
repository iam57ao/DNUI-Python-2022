def isleap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def yesterday(date):
    year, month, day = map(int, date.split("-"))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        days[1] = 29
    if day == 1:
        if month == 1:
            year -= 1
            month = 12
            day = 31
        else:
            month -= 1
            day = days[month - 1]
    else:
        day -= 1
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"


for count in range(int(input())):
    print(yesterday(input()))
