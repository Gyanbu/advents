with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
print(data)


gears = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '*':
            gears[(i, j)] = []
print(gears)

indexed_numbers = []
for i, line in enumerate(data):
    buf = ''
    for j, char in enumerate(line):
        if char.isdigit():
            buf += char
            if j == len(line) - 1:
                indexed_numbers.append((i, j - len(buf) + 1, j + 1))
        elif buf:
            indexed_numbers.append((i, j - len(buf), j))
            buf = ''


for num in indexed_numbers:
    done = False
    for i in range(num[0] - 1, num[0] + 2):
        if done:
            break

        if i < 0 or i >= len(data):
            continue

        for j in range(num[1] - 1, num[2] + 1):
            if j < 0 or j >= len(data[0]):
                continue

            if i == num[0] and num[1] <= j < num[2]:
                continue

            if data[i][j] == '*':
                gears[(i, j)].append(int(data[num[0]][slice(num[1], num[2])]))
                done = True
                break
print(gears)

answer = 0
for gear in gears.values():
    if len(gear) == 2:
        answer += gear[0] * gear[1]
print(answer)
