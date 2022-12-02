import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


q = 34000000

n = 0
# highest_lowest_gifts = 0
while True:
    n += 1
    if not is_prime(n):
        continue
    gifts_received = n * 10
    for i in range(n):
        if i > n // 2:
            print(f'\n[{n}]: {i}')
            break
        if n % (i + 1) == 0:
            gifts_received += (i + 1) * 10

    print(gifts_received)
    if gifts_received >= q:
        break
print(n)
