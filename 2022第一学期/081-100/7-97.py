people, num = map(int, input().split())
people_list = list(range(1, people + 1))
end_list = []
index = 0
while people_list:
    index = (index + num - 1) % len(people_list)
    end_list.append(people_list.pop(index))
print(*end_list)