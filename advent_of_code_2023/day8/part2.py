import math


with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

directions = []
for direction in data[0]:
    if direction == 'L':
        directions.append(0)
    else:
        directions.append(1)


# print(directions)


def direction_gen(directions):
    for direction in directions:
        yield direction


def join_lists_in_list(input_list):
    buf = []
    for inner_list in input_list:
        buf.extend(inner_list)
    return buf


nodes = {}
for node in data[2:]:
    nodes[node[0:3]] = (node[7:10], node[12:15])
# print(nodes)

locations = []
for location in nodes.keys():
    if location[2] == 'A':
        locations.append(location)
# print(locations)


paths = {}
for ghost in locations:
    paths[ghost] = []
    location = ghost
    while True:
        buf = []
        for direction in direction_gen(directions):
            location = nodes[location][direction]
            buf.append(location)
        if buf in paths[ghost]:
            loop_start = paths[ghost].index(buf)
            pre_loop = join_lists_in_list(paths[ghost][:loop_start])
            loop = join_lists_in_list(paths[ghost][loop_start:])

            z_mod = []
            for i, node in enumerate(loop):
                if node[-1] == 'Z':
                    z_mod.append(i + 1)

            paths[ghost] = [pre_loop, loop, len(pre_loop) + min(z_mod)]
            break
        paths[ghost].append(buf)
    print(
        f'[{ghost}]\n'
        f'Pre loop: {len(paths[ghost][0])}\n'
        f'Loop: {len(paths[ghost][1])}\n'
        f'First z: {paths[ghost][2]}\n'
    )
    # I guess last item in loop is z?

pre_loop = 1
for ghost in paths:
    if pre_loop != len(paths[ghost][0]):
        pre_loop *= len(paths[ghost][0])

locations = []
steps = []
for ghost in paths:
    locations.append(paths[ghost][2])
    steps.append(len(paths[ghost][1]))
print(locations)
print(math.lcm(*locations))
