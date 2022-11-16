def isprime(x):
    if x != 1:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False


num = int(input())
for j in range(2, num):
    if isprime(j) and isprime(num - j):
        print(f"{num} = {j} + {num - j}")
        break
