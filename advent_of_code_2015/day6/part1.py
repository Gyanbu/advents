with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]


import array_to_image
array = []
for _ in range(1000):
    array.append([False] * 1000)

# data = ['turn on 1,1 through 2,2']
for instruction in data:
    instruction = instruction.split()
    if instruction[0] == 'toggle':
        x1, y1 = instruction[1].split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = instruction[3].split(',')
        x2, y2 = int(x2), int(y2)

        x_len = max(x1, x2) - min(x1, x2) + 1
        y_len = max(y1, y2) - min(y1, y2) + 1

        for x in range(x_len):
            for y in range(y_len):
                array[min(x1, x2) + x][min(y1, y2) + y] = not array[min(x1, x2) + x][min(y1, y2) + y]
    else:
        x1, y1 = instruction[2].split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = instruction[4].split(',')
        x2, y2 = int(x2), int(y2)

        x_len = max(x1, x2) - min(x1, x2) + 1
        y_len = max(y1, y2) - min(y1, y2) + 1

        if instruction[1] == 'on':
            for x in range(x_len):
                for y in range(y_len):
                    array[min(x1, x2) + x][min(y1, y2) + y] = True
        else:
            for x in range(x_len):
                for y in range(y_len):
                    array[min(x1, x2) + x][min(y1, y2) + y] = False

answer = 0
for row in array:
    for col in row:
        if col:
            answer += 1
print(answer)

image = array_to_image.convert(array)
image.save('part1.png', 'PNG')
