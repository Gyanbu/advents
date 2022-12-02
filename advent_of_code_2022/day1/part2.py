with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
# print(data)

data_sorted = []
buf = []
for line in data:
    if line != '':
        buf.append(int(line))
    else:
        data_sorted.append(buf)
        buf = []
# print(data_sorted)


elfs_sorted = []
for elf in data_sorted:
    elfs_sorted.append(sum(elf))
elfs_sorted = sorted(elfs_sorted, reverse=True)
# print(elfs_sorted)

answer = 0
for i in range(3):
    answer += elfs_sorted[i]
print(answer)
