score = int(input())
level = "E"
if score >= 90:
    level = "A"
elif 80 <= score < 90:
    level = "B"
elif 70 <= score < 80:
    level = "C"
elif 60 <= score < 70:
    level = "D"
print(level)
