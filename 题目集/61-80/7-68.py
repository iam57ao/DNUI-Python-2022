speed, limit = map(int, input().split())
state = "OK"
per = (speed - limit) / limit
if speed > limit and 0.1 <= per < 0.5:
    state = f"Exceed {per * 100:.0f}%. Ticket 200"
elif per >= 0.5:
    state = f"Exceed {per * 100:.0f}%. License Revoked"
print(state)
