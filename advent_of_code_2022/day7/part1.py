with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

# with open('test_data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)


import re
max_file_size = 100000


def add_directory_to_tree(tree, path, name):
    for d, dir in enumerate(path):
        if d == 0:
            buf = tree[dir]
        else:
            buf = buf[0][dir]

    if not buf[0].get(name, False):
        buf[0][name] = [{}, 0]


def add_file_to_directory(tree, path, name, size):
    for d, dir in enumerate(path):
        if d == 0:
            buf = tree[dir]
        else:
            buf = buf[0][dir]
        buf[1] += size

    buf[0][name] = size


directories_tree = {'/': [{}, 0]}
path = []
for line in data:
    buf = line.split(' ')
    if buf[0] == '$':
        if buf[1] == 'cd':
            if buf[2] == '':
                path = []
            elif buf[2] == '..':
                path.pop()
            else:
                path.append(buf[2])

    else:  # ls
        if buf[0] == 'dir':
            # if not directories_tree.get(buf[0], False):
            add_directory_to_tree(directories_tree, path, buf[1])
        else:  # file
            add_file_to_directory(directories_tree, path, buf[1], int(buf[0]))
print(directories_tree)

result = re.findall(', (\d+)', str(directories_tree.values()))
answer = 0
for size in result:
    if int(size) <= max_file_size:
        answer += int(size)
print(answer)
