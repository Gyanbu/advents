with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


answer = 0
for group in data:
    buf = group.split(',')
    for i, elf in enumerate(buf):
        buf[i] = tuple(int(n) for n in elf.split('-'))

    for n in range(buf[0][0], buf[0][1] + 1):
        if buf[1][0] <= n <= buf[1][1]:
            answer += 1
            break
print(answer)
