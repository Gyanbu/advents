# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


pairs = []
buf = []
for line in data:
    if line == '':
        pairs.append(buf)
        buf = []
        continue

    buf.append(eval(line))
pairs.append(buf)

answer = 0
for p, pair in enumerate(pairs):
    pair1 = pair[0]
    pair2 = pair[1]

    while True:
        if not pair1:
            answer += p + 1
            break
        if not pair2:
            break

        buf1 = pair1.pop()
        buf2 = pair2.pop()

        if
