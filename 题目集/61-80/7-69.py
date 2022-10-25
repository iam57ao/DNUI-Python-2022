import math
weight, state = input().split()
cost = 8
if int(weight) > 1000:
    cost += math.ceil((int(weight) - 1000) / 500) * 4
if state == "y":
    cost += 5
print(cost)
