from math import sqrt

# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


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
    #     return

    x_diff = tail[0] - head[0]
    y_diff = tail[1] - head[1]

    if x_diff == 2 and y_diff == 2:
        tail[0] -= 1
        tail[1] -= 1
        return
    if x_diff == 2 and y_diff == -2:
        tail[0] -= 1
        tail[1] += 1
        return
    if x_diff == -2 and y_diff == 2:
        tail[0] += 1
        tail[1] -= 1
        return
    if x_diff == -2 and y_diff == -2:
        tail[0] += 1
        tail[1] += 1
        return

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
tail1 = [0, 0]
tail2 = [0, 0]
tail3 = [0, 0]
tail4 = [0, 0]
tail5 = [0, 0]
tail6 = [0, 0]
tail7 = [0, 0]
tail8 = [0, 0]
tail9 = [0, 0]

answer = []
for instruction in data:
    for _ in range(instruction[1]):
        move_head(head, instruction[0])
        move_tail(head, tail1)
        move_tail(tail1, tail2)
        move_tail(tail2, tail3)
        move_tail(tail3, tail4)
        move_tail(tail4, tail5)
        move_tail(tail5, tail6)
        move_tail(tail6, tail7)
        move_tail(tail7, tail8)
        move_tail(tail8, tail9)
        print(tail9)
        if tail9 not in answer:
            answer.append(tail9.copy())
print(len(answer))
