x, y = map(int, input().split(","))
location = "第一象限"
if x > 0 and y < 0:
    location = "第四象限"
elif x < 0 and y > 0:
    location = "第二象限"
elif x < 0 and y < 0:
    location = "第三象限"
print(location)
