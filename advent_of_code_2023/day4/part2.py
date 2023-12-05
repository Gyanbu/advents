with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

data = [line.split(': ')[1].split(' | ') for line in data]
for i in range(len(data)):
    data[i] = [[int(num) for num in data[i][0].split()], [int(num) for num in data[i][1].split()]]
# print(data[0])


for c, card in enumerate(data):
    value = 0
    for num in card[1]:
        if num in card[0]:
            value += 1
    data[c] = [value, 1]
print(data)

for i, card in enumerate(data):
    for j, value in enumerate(range(card[0])):
        data[i + j + 1][1] += card[1]
print(data)

answer = 0
for card in data:
    answer += card[1]
print(answer)
