with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
# print(data[0:4])

result = 0
for line in data:
    first = None
    last = None
    for char in line:
        if char.isdigit():
            if first is None:
                first = int(char)
            else:
                last = int(char)

    if last is None:
        last = first

    result += first * 10 + last
print(result)