with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

# with open('test_data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)


instructions = [0]
for line in data:
    if 'addx' in line:
        instructions.append(int(line[5:]))
    else:
        instructions.append(0)
print(instructions)

buffer = []
x = 1
for instruction in instructions:
    buf = ''
    if instruction == 0:
        buffer.append(x)
    else:
        buffer.append(x)
        x += instruction
        buffer.append(x)
print(buffer)


for i, x in enumerate(buffer):
    if i % 40 == 0:
        print()
    if i % 40 in (x - 1, x, x + 1):
        print('#', end='')
    else:
        print('.', end='')
