from PIL import Image

with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

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


def tree_visible(tree_x, tree_y, array2d):
    array_size = len(array2d)

    edge = (0, array_size - 1)
    if tree_x in edge or tree_y in edge:
        return True

    taller_tree = False
    for x in range(0, tree_x):
        # print(f'Left: {x}, {tree_y} -> {array2d[x][tree_y]}')
        if array2d[x][tree_y] >= array2d[tree_x][tree_y]:
            taller_tree = True
            break
    if taller_tree is False:
        return True

    taller_tree = False
    for x in range(tree_x + 1, array_size):
        # print(f'Right: {x}, {tree_y} -> {array2d[x][tree_y]}')
        if array2d[x][tree_y] >= array2d[tree_x][tree_y]:
            taller_tree = True
            break
    if taller_tree is False:
        return True

    taller_tree = False
    for y in range(0, tree_y):
        # print(f'Up: {tree_x}, {y} -> {array2d[tree_x][y]}')
        if array2d[tree_x][y] >= array2d[tree_x][tree_y]:
            taller_tree = True
            break
    if taller_tree is False:
        return True

    taller_tree = False
    for y in range(tree_y + 1, array_size):
        # print(f'Down: {tree_x}, {y} -> {array2d[tree_x][y]}')
        if array2d[tree_x][y] >= array2d[tree_x][tree_y]:
            taller_tree = True
            break
    if taller_tree is False:
        return True
    return False


array2d = create_2d_array(data)


image = Image.new('1', (len(array2d), len(array2d[0])))
pixels = image.load()


answer = 0
for y in range(len(array2d)):
    print()
    for x in range(len(array2d)):
        # print(array2d[x][y], end='')
        if tree_visible(x, y, array2d):
            answer += 1
            print('V', end='')
            pixels[x, y] = 1
        else:
            print('H', end='')
            pixels[x, y] = 0
print()
print(answer)

image.save('part1.png', 'PNG')
