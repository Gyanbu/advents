# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


m = 0
monkeys = []
for line in data:
    if 'Monkey' in line:
        m = int(line[7:-1])
        monkeys.append({})

    if 'Starting items:' in line:
        monkeys[m]['Items'] = list(map(int, line[16:].split(', ')))

    if 'Operation:' in line:
        if '*' in line:
            try:
                monkeys[m]['Operation'] = ('*', int(line.split('* ')[1]))
            except ValueError:
                monkeys[m]['Operation'] = ('*', 'old')
        elif '+' in line:
            try:
                monkeys[m]['Operation'] = ('+', int(line.split('+ ')[1]))
            except ValueError:
                monkeys[m]['Operation'] = ('+', 'old')
        else:
            raise 'Not supported math'

    if 'Test' in line:
        monkeys[m]['Test'] = int(line[19:])

    if 'true' in line:
        monkeys[m]['True'] = int(line[25:])

    if 'false' in line:
        monkeys[m]['False'] = int(line[26:])
print(monkeys)

