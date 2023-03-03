import math
x = float(input())
value = 0
if x > 3.5:
    value = math.cos(x) + math.e ** x
elif 0 < x <= 3.5:
    value = math.tan(x) + math.log(1 + x)
print(f"{value:.2f}")
