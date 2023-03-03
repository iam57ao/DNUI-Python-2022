h, m = map(int, input().split(":"))
if h > 12:
    h = h-12
    print(f"{h}:{m} PM")
elif h == 12:
    print(f"{h}:{m} PM")
elif h == 0:
    print(f"{12}:{m} AM")
else:
    print(f"{h}:{m} AM")
