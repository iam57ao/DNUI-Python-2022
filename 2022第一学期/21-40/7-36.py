a, b, c, d = map(int, input().split())
h, m = 0, 0
if 0 <= a < c <= 24 and b <= 60 and d <= 60:
    play_min = (c * 60 + d) - (a * 60 + b)
    print(f"{play_min // 60}:{play_min % 60}")
else:
    exit()
