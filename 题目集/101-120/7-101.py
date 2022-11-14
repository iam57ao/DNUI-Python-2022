from sys import stdin


def horse_count(num):
    count_list = []
    for big_horse in range(num // 3 + 3):
        for middle_horse in range(num // 2 + 2):
            for small_horse in range(0, num // 2 * 2, 2):
                if big_horse * 3 + middle_horse * 2 + small_horse / 2 == num and big_horse + middle_horse + small_horse == num:
                    count_list.append(f"{big_horse} {middle_horse} {small_horse}")
    for i in count_list:
        print(i)


num_input = list(map(int, stdin.read().split()))
for element in num_input:
    horse_count(element)
