with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


groups = []
answer = 0
for group in data:
    buf = group.split(',')
    for i, pair in enumerate(buf):
        sectors = pair.split('-')
        buf[i] = ''
        for n in range(int(sectors[0]), int(sectors[1]) + 1):
            buf[i] += f'{n},'
    if buf[0] in buf[1] or buf[1] in buf[0]:
        answer += 1
print(answer)
