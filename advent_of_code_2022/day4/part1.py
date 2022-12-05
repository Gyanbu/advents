with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


answer = 0
for group in data:
    buf = group.split(',')
    for i, elf in enumerate(buf):
        buf[i] = tuple(int(n) for n in elf.split('-'))

    if buf[0][0] >= buf[1][0] and buf[0][1] <= buf[1][1]:
        answer += 1
    elif buf[1][0] >= buf[0][0] and buf[1][1] <= buf[0][1]:
        answer += 1
print(answer)
