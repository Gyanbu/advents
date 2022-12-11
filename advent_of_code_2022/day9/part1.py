from math import sqrt

with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

# with open('test_data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
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


def move_tail(head, tail):
    # distance = sqrt((tail[0] - head[0]) ** 2 + (tail[1] - head[1]) ** 2)
    # if distance < 1.5:
    #     return False

    x_diff = tail[0] - head[0]
    y_diff = tail[1] - head[1]

    if x_diff == 2:
        tail[0] -= 1
        tail[1] = head[1]
    if x_diff == -2:
        tail[0] += 1
        tail[1] = head[1]

    if y_diff == 2:
        tail[1] -= 1
        tail[0] = head[0]
    if y_diff == -2:
        tail[1] += 1
        tail[0] = head[0]

for i, instruction in enumerate(data):
    data[i] = instruction.split(' ')
    data[i][1] = int(data[i][1])
print(data)

head = [0, 0]
tail = [0, 0]

answer = []
for instruction in data:
    for _ in range(instruction[1]):
        move_head(head, instruction[0])
        move_tail(head, tail)
        if tail not in answer:
            answer.append(tail.copy())
print(len(answer))