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

step = 0
location = 'AAA'
destination = 'ZZZ'
for direction in direction_gen(directions):
    step += 1
    location = nodes[location][direction]
    if location == 'ZZZ':
        break
print(step)
