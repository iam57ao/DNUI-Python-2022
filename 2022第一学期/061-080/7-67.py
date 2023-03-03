weight = float(input())
cost = 0
if weight < 20:
    cost = 12 + (weight - 1) * 2
elif 20 <= weight < 60:
    cost = 39 + (weight - 20) * 1.9
else:
    cost = 115 + (weight - 60) * 1.3
print(int(cost+0.5))