n = int(input())
num = list(map(int, input().split()))
avg = sum(num) / n
a = 0
i = 0
while i < n:
    a += (num[i] - avg) ** 2
    i += 1
print(f"{(a / n) ** 0.5:.5f}")
