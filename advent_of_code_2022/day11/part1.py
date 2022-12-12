with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)

# with open('test_data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)


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

monkey_business = [0] * len(monkeys)
for _ in range(20):
    for m, monkey in enumerate(monkeys):
        for _ in range(len(monkey['Items'])):
            monkey_business[m] += 1

            item = monkey['Items'].pop(0)
            if monkey['Operation'][0] == '*':
                if monkey['Operation'][1] == 'old':
                    item *= item
                else:
                    item *= monkey['Operation'][1]
            elif monkey['Operation'][0] == '+':
                if monkey['Operation'][1] == 'old':
                    item += item
                else:
                    item += monkey['Operation'][1]

            item //= 3

            if item % monkey['Test'] == 0:
                monkeys[monkey['True']]['Items'].append(item)
            else:
                monkeys[monkey['False']]['Items'].append(item)

monkey_business = sorted(monkey_business, reverse=True)
print(monkey_business[0] * monkey_business[1])
