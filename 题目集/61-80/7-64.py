speed = int(input())
limit = int(input())
state = "未超速"
if speed <= limit:
    print(state)
else:
    per = (speed - limit) / limit
    if per <= 0.1:
        state = "超速警告"
    elif 0.1 < per <= 0.2:
        state = "罚款100元"
    elif 0.2 < per <= 0.5:
        state = "罚款500元"
    elif 0.5 < per <= 1:
        state = "罚款1000元"
    else:
        state = "罚款2000元"
    print(state)
