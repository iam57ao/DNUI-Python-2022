teamA = {1, 2, 3, 4, 5}
teamB = {6, 7, 8, 9, 10}
get = set(map(int, input().split(",")))
print(*sorted(teamB - get))