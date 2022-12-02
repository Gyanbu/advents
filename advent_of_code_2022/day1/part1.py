with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

data_sorted = []
buf = []
for line in data:
    if line != '':
        buf.append(int(line))
    else:
        data_sorted.append(buf)
        buf = []
print(data_sorted)


thickest = 0
for elf in data_sorted:
    if sum(elf) > thickest:
        thickest = sum(elf)
print(thickest)
