import string
from functools import cache

# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(f'{data}')


alphabet = string.ascii_letters
print(alphabet)

terrain = []
for line in data:
    terrain.append([alphabet.index(letter) for letter in line])
print(terrain)

for j, y in enumerate(terrain):
    for i, x in enumerate(y):
        if x == 44:
            y[i] = alphabet.index('a')
            start = (i, j)
        elif x == 30:
            y[i] = alphabet.index('z')
            end = (i, j)
print(terrain)
print(f'{start = }\n{end = }')


def path(start=None, end=None, terrain=None, pos=None, path=[], visited=[]):
    if start is not None:
        pos = start

    if pos[0] != 0:
        if terrain[pos[0] - 1, pos[1]] - terrain[pos[0], pos[1]] <= 1:
            visited_copy = visited.copy()
            visited_copy.append()
            path()


path(start=start, end=end, terrain=terrain)
