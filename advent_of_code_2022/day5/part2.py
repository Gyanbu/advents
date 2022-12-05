with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()][10:]
    # data = f.readlines()
# print(data)

containers = [
    ['h', 'c', 'r'],
    ['b', 'j', 'h', 'l', 's', 'f'],
    ['r', 'm', 'd', 'h', 'j', 't', 'q'],
    ['s', 'g', 'r', 'h', 'z', 'b', 'j'],
    ['r', 'p', 'f', 'z', 't', 'd', 'c', 'b'],
    ['t', 'h', 'c', 'g'],
    ['s', 'n', 'v', 'z', 'b', 'p', 'w', 'l'],
    ['r', 'j', 'q', 'g', 'c'],
    ['l', 'd', 't', 'r', 'h', 'p', 'f', 's']
]

instructions = []
for line in data:
    buf = line.split('move ')[1].split(' from ')
    buf[0] = int(buf[0])
    for i in buf.pop().split(' to '):
        buf.append(int(i))
    # print(buf)
    instructions.append(buf)


for instruction in instructions:
    amount, start, end = instruction[0], instruction[1] - 1, instruction[2] - 1
    buf = []

    for _ in range(amount):
        buf.append(containers[start].pop())
    for crate in buf[::-1]:
        containers[end].append(crate)

for container in containers:
    if len(container) > 0:
        print(container[-1].upper(), end='')
