import sys
line = sys.stdin.read().split("\n")
num = []
for x in range(len(line)):
    if line[x].isdigit():
        num.append(line[x])
num = list(map(int, num))
print(max(num), min(num), f"{sum(num) / len(num):.2f}")
