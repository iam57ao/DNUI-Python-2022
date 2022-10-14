a = list(input())
i = 0
o = ""
while i < len(a):
    a[i] = ord(a[i])
    i += 1
print(*a)
