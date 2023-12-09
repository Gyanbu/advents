with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

data = [[int(num) for num in line.split()] for line in data]
print(data)


def get_next_value_of_sequence(sequence):
    history = [sequence]
    i = 0
    while True:
        buf = []
        for j in range(len(history[i]) - 1):
            buf.append(history[i][j + 1] - history[i][j])
        if len(buf) == buf.count(0):  # or len(buf) == 1:
            break
        history.append(buf)
        i += 1

    next_value = history[-1][0]
    for i in range(len(history) - 2, -1, -1):
        next_value = history[i][0] - next_value
    return next_value


# data = [[10, 13, 16, 21, 30, 45]]
result = 0
for sequence in data:
    result += get_next_value_of_sequence(sequence)
print(result)
