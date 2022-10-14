y, m, d = map(int, input().split())
print(f"{(((y / 100) // 4 - 2 * (y / 100) + y + y // 4 + (13 * (m + 1)) // 5 + d - 1) % 7) // 1:.0f}")
