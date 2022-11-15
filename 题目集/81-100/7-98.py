numerator = 1
denominator = 1
count = 1
sum_value = 1
eps = float(input())
while numerator / denominator > eps:
    numerator *= count
    denominator *= 2 * count + 1
    sum_value += numerator / denominator
    count += 1
print(f"PI = {sum_value * 2:.5f}")