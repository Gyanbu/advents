with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

directions = []
for direction in data[0]:
    if direction == 'L':
        directions.append(0)
    else:
        directions.append(1)
print(directions)


def direction_gen(directions):
    while True:
        for direction in directions:
            yield direction


nodes = {}
for node in data[2:]:
    nodes[node[0:3]] = (node[7:10], node[12:15])
print(nodes)

locations = []
for location in nodes.keys():
    if location[2] == 'A':
        locations.append(location)
print(locations)


step = 0
destination = 'Z'
for direction in direction_gen(directions):
    step += 1
    all_z = True
    for l, location in enumerate(locations):
        locations[l] = nodes[location][direction]
        if location[2] != destination:
            all_z = False
    if all_z:
        break
    print(step - 1)
