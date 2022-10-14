a = int(input())
b = list(map(int, input().split()))
b.sort()
if a % 2 != 0:
    print(max(b) + min(b) + b[(a+1) // 2 - 1])
else:
    print(max(b) + min(b) + b[a // 2 - 1])
