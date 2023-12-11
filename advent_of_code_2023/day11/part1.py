# with open('data.txt', 'rt') as f:
with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

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

for r in range(len(row_empty) - 1, -1, -1):
    if row_empty[r]:
        data.insert(r, ['.'] * len(data[0]))

for c in range(len(col_empty) - 1, -1, -1):
    if col_empty[c]:
        for row in data:
            row.insert(c, '.')

galaxies = {}
g = 0
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == '#':
            galaxies[g] = (r, c)
            g += 1
print(galaxies)


def get_distance(p1, p2):
    while p1 != p2:
        x_diff = abs(p2[0] - p1[0])
        y_diff = abs(p2[1] - p1[1])

        if x_diff > y_diff:
