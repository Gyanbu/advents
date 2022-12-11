# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
# print(data)


def move_head(position, direction):
    if direction == 'L':
        position[0] -= 1
    elif direction == 'R':
        position[0] += 1
    elif direction == 'D':
        position[1] -= 1
    elif direction == 'U':
        position[1] += 1


for i, instruction in enumerate(data):
    data[i] = instruction.split(' ')
    data[i][1] = int(data[i][1])
print(data)

head = [0, 0]
tail = [0, 0]

for instruction in data:
    for _ in range(instruction[1]):
        move_head(head, instruction[0])

        print(head)