import sys
a = list(map(int, sys.stdin.readlines()))
print(max(a), min(a), f"{sum(a) / len(a):.2f}")
