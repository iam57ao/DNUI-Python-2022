repeat = 0
line_num = int(input())
for line in range(line_num):
    line_list = input().split()
    if len(line_list) != len(set(line_list)):
        repeat += 1
print(f"True={repeat}, False={line_num - repeat}")