import string

with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


alphabet = string.ascii_letters
bags = []
for bag in data:
    buf = [[], []]
    for letter in bag[:len(bag) // 2]:
        buf[0].append(alphabet.index(letter))
    for letter in bag[len(bag) // 2:]:
        buf[1].append(alphabet.index(letter))
    bags.append(buf)
print(bags)


answer = 0
for bag in bags:
    for item in bag[0]:
        if item in bag[1]:
            answer += item
            break
print(answer)
