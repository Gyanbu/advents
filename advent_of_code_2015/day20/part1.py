q = 34000000

n = 0
# highest_lowest_gifts = 0
while True:
    n += 1
    gifts_received = 0
    for i in range(n):
        if n % (i + 1) == 0:
            gifts_received += (i + 1) * 10
    if gifts_received >= q:
        break
    print(gifts_received)
print(gifts_received)
