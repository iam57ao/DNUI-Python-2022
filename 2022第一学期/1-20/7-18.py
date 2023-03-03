a, b, c = map(int, input().split())
if a + b > c:
    p = (a + b + c) / 2
    print("面积是：%.2f" % (p * (p - a) * (p - b) * (p - c)) ** (1 / 2))
else:
    print("不能构成三角形")
