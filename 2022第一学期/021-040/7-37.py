a = int(input())
b = list(map(str, input().split()))
print(*b[a-1:] + b[:a-1])
