with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
# print(data)

# with open('test_data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)


def create_2d_array(array):
    array_to_return = []
    for _ in range(len(array)):
        array_to_return.append([None] * len(array))

    for l, line in enumerate(array):
        for n, number in enumerate(line):
            array_to_return[n][l] = int(number)

    return array_to_return


def tree_scenic_score(tree_x, tree_y, array2d):
    array_size = len(array2d)

    edge = (0, array_size - 1)
    if tree_x in edge or tree_y in edge:
        return 0

    scenic_score = 1

    buf = 0
    for x in reversed(range(0, tree_x)):
        # print(f'Left: {x}, {tree_y} -> {array2d[x][tree_y]}')
        if array2d[x][tree_y] >= array2d[tree_x][tree_y]:
            buf += 1
            break
        else:
            buf += 1
    scenic_score *= buf

    buf = 0
    for x in range(tree_x + 1, array_size):
        # print(f'Right: {x}, {tree_y} -> {array2d[x][tree_y]}')
        if array2d[x][tree_y] >= array2d[tree_x][tree_y]:
            buf += 1
            break
        else:
            buf += 1
    scenic_score *= buf

    buf = 0
    for y in reversed(range(0, tree_y)):
        # print(f'Up: {tree_x}, {y} -> {array2d[tree_x][y]}')
        if array2d[tree_x][y] >= array2d[tree_x][tree_y]:
            buf += 1
            break
        else:
            buf += 1
    scenic_score *= buf

    buf = 0
    for y in range(tree_y + 1, array_size):
        # print(f'Down: {tree_x}, {y} -> {array2d[tree_x][y]}')
        if array2d[tree_x][y] >= array2d[tree_x][tree_y]:
            buf += 1
            break
        else:
            buf += 1
    scenic_score *= buf

    return scenic_score


array2d = create_2d_array(data)

answer = 0
for y in range(len(array2d)):
    for x in range(len(array2d)):
        if tree_scenic_score(x, y, array2d) > answer:
            answer = tree_scenic_score(x, y, array2d)
print(answer)