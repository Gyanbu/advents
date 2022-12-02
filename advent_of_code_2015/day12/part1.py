with open('data.txt', 'rt') as f:
    data = f.readline().strip()


answer = 0
buffer = 0
m = 1
for char in reversed(data):
    try:
        buffer += m * int(char)
        m *= 10
    except ValueError:
        if char == '-':
            answer -= buffer
        else:
            answer += buffer
        buffer = 0
        m = 1
print(answer)
