from sys import stdin
date_list = stdin.readlines()
out_list = sorted(date_list, key=lambda date: (date.split("/")[2], date.split("/")[0], date.split("/")[1]))
for out in out_list:
    print(out.strip())