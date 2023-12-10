with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

data = [[pipe for pipe in line] for line in data]
print(data)


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
    'S': False
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


path = []
while True:
    offset = direction(location[2])
    print(data[location[1] + offset[1]][location[0] + offset[0]])
    pipe = pipes[data[location[1] + offset[1]][location[0] + offset[0]]]
    if not pipe:
        break
    location = [location[0] + offset[0], location[1] + offset[1], pipe[location[2]]]
    path.append(location)
print(path)
print(len(path) // 2 + 1)
