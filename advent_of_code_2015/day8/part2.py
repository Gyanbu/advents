with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

#data = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
#data = ['"\\x27"']
answer = 0
for word in data:
    escape = False
    ignore = 0
    real_len = len(word) + 4
    for char in word[1:-1]:
        # print(char)
        if ignore > 0:
            ignore -= 1
            real_len += 1
        elif escape:
            escape = False
            if char == 'x':
                ignore = 2
                real_len -= 3
        elif char == '\\':
            escape = True
            real_len += 2

        # print(f'{char}, {real_len}')
    print(f'{real_len}, {len(word)}\n')
    answer += real_len - len(word)
print(answer)
