import string

# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


alphabet = string.ascii_letters
print(alphabet)

height_map = []
steps_map = []
for y, row in enumerate(data):
    buf = []
    for x, letter in enumerate(row):
        if letter == 'S':
            start = (x, y)
            buf.append(alphabet.index('a'))
        elif letter == 'E':
            end = (x, y)
            buf.append(alphabet.index('z'))
        else:
            buf.append(alphabet.index(letter))
    height_map.append(buf)
    steps_map.append([float('inf')] * len(buf))
steps_map[start[1]][start[0]] = 0
print(f'{height_map = }\n{steps_map = }\n{start = }\n{end = }')


def check_neighbors(pos, steps_map):
    pos_x, pos_y = pos
    steps = steps_map[pos_y][pos_x]
    height = height_map[pos_y][pos_x]
    for x, y in (pos_x - 1, pos_y), (pos_x + 1, pos_y), (pos_x, pos_y - 1), (pos_x, pos_y + 1):
        if x < 0 or y < 0 or x > len(steps_map[0]) - 1 or y > len(steps_map) - 1 or steps_map[y][x] != float('inf'):
            continue

        if height + 1 >= height_map[y][x]:
            steps_map[y][x] = steps + 1
            check_neighbors((x, y), steps_map)
        # print(f'{x}, {y}')


check_neighbors(start, steps_map)
print(steps_map[end[1]][end[0]])
for line in steps_map:
    print(line)
