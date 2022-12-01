def is_prime(input_num):
    if input_num == 1:
        return False
    for i in range(2, int(input_num ** 0.5) + 1):
        if input_num % i == 0:
            return False
    else:
        return True


def is_symmetry(input_num):
    if str(input_num) == str(input_num)[::-1]:
        return True
    else:
        return False


while True:
    try:
        num = int(input())
    except EOFError:
        break
    else:
        if is_prime(num) and is_symmetry(num) and len(str(num)) <= 5:
            print("Yes")
        else:
            print("No")

