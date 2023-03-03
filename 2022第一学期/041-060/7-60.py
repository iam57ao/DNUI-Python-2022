a, b = map(float, input().split())
if a > 50:
    print(f"cost = {(a - 50) * b + 50 * 0.53:.2f}")
else:
    print(f"cost = {a * 0.53:.2f}")
