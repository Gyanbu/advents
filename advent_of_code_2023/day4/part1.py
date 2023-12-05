with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

data = [line.split(': ')[1].split(' | ') for line in data]
for i in range(len(data)):
    data[i] = [[int(num) for num in data[i][0].split()], [int(num) for num in data[i][1].split()]]
print(data[0])

answer = 0
for card in data:
    value = 0
    for num in card[1]:
        if num in card[0]:
            if value == 0:
                value = 1
            else:
                value *= 2
    answer += value
print(answer)
