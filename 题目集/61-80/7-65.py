x = float(input())
y = 0
if 0 <= x < 5:
    y = x
elif 5 <= x < 10:
    y = 3 * x - 5
elif 10 <= x < 20:
    y = 0.5 * x - 2
print("x={:.2f},y={:.2f}".format(x, y))
