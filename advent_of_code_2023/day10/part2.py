import sys

with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

data = [[pipe for pipe in line] for line in data]
# print(data)


# 0 up, 1 right, 2 down, 3 left
pipes = {
    '|': {
        0: 0,
        2: 2
    },
    '-': {
        1: 1,
        3: 3
    },
    'L': {
        2: 1,
        3: 0
    },
    'J': {
        1: 0,
        2: 3
    },
    '7': {
        0: 3,
        1: 2
    },
    'F': {
        0: 1,
        3: 2
    },
    'S': {
        0: 3,
        1: 2
    }
}

animal = None
for y, line in enumerate(data):
    for x, pipe in enumerate(line):
        if pipe == 'S':
            animal = (x, y)
if not animal:
    raise "No animal somehow lul"

if data[animal[1] - 1][animal[0]] in '|7F':
    location = [animal[0], animal[1], 0]
elif data[animal[1]][animal[0] + 1] in '-J7':
    location = [animal[0], animal[1], 1]
elif data[animal[1] + 1][animal[0]] in '|LJ':
    location = [animal[0], animal[1], 2]
else:
    location = [animal[0], animal[1], 3]


def direction(num):
    if num == 0:
        return [0, -1]
    elif num == 1:
        return [1, 0]
    elif num == 2:
        return [0, 1]
    return [-1, 0]


path = [location[0:2] + [data[location[1]][location[0]]]]
while True:
    offset = direction(location[2])
    if data[location[1] + offset[1]][location[0] + offset[0]] == 'S':
        break
    pipe = pipes[data[location[1] + offset[1]][location[0] + offset[0]]]
    location = [location[0] + offset[0], location[1] + offset[1], pipe[location[2]]]
    pipe_type = data[location[1]][location[0]]
    path.append(location[0:2] + [pipe_type])
# print(path)


height = len(data)
width = len(data[0])

board = []
for _ in range(2 * height - 1):
    board.append(['.'] * (2 * width - 1))

for pipe in path:
    board[pipe[1] * 2][pipe[0] * 2] = pipe[2]
    for num in pipes[pipe[2]].values():
        d = direction(num)
        if d[0]:
            board[pipe[1] * 2][pipe[0] * 2 + d[0]] = '-'
        else:
            board[pipe[1] * 2 + d[1]][pipe[0] * 2] = '|'


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()


# print_board(board)


def flood_fill(x, y):
    board[y][x] = ' '
    for offset in (-1, 1):
        if 0 < x + offset < len(board[0]) and board[y][x + offset] == '.':
            flood_fill(x + offset, y)
        if 0 < y + offset < len(board) and board[y + offset][x] == '.':
            flood_fill(x, y + offset)


sys.setrecursionlimit(100000)

for y in range(len(board)):
    if board[y][0] == '.':
        flood_fill(0, y)
    if board[y][len(board[0]) - 1] == '.':
        flood_fill(len(board[0]) - 1, y)

print_board(board)
board = board[::2]
board = [row[::2] for row in board]
print_board(board)

result = 0
for row in board:
    for char in row:
        if char == '.':
            result += 1
print(result)
