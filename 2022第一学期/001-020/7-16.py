a, b, c = map(int, input().split())
print(f"x1={(- b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a):.1f}")
print(f"x2={(- b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a):.1f}")
