with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

years = 1000000 - 1
data = [list(row) for row in data]


def print_board():
    for row in data:
        for char in row:
            print(char, end='')
        print()


row_empty = [True] * len(data)
col_empty = [True] * len(data[0])
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char != '.':
            row_empty[r] = False
            col_empty[c] = False
# print(row_empty)
# print(col_empty)

galaxies = []
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == '#':
            galaxies.append([r, c])
print(galaxies)


for offset in range(len(row_empty) - 1, -1, -1):
    if row_empty[offset]:
        for galaxy in galaxies:
            if galaxy[0] > offset:
                galaxy[0] += years

for offset in range(len(col_empty) - 1, -1, -1):
    if col_empty[offset]:
        for galaxy in galaxies:
            if galaxy[1] > offset:
                galaxy[1] += years

# print_board()

def get_distance(p1, p2):
    distance = max(p1[0], p2[0]) - min(p1[0], p2[0]) + max(p1[1], p2[1]) - min(p1[1], p2[1])
    return distance


result = 0
for g, galaxy in enumerate(galaxies):
    for i in range(g + 1, len(galaxies)):
        distance = get_distance(galaxy, galaxies[i])
        result += distance
        # print(f'{galaxy, galaxies[i]} -> {distance}')
print(result)
