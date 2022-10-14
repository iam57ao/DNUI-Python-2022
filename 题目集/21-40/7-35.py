a = list(map(str, input().split()))
i = 0
num = 0
while i != len(a):
    num += len(a[i])
    i += 1
print(f"{len(a)},{num/len(a):.2f}")
