with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

result = 0
for line in data:
    first = [len(line), None]
    last = [0, None]
    for num in nums:
        i = line.find(num)
        if i != -1 and i < first[0]:
            first[0] = i
            first[1] = nums.index(num)

        i = line.rfind(num)
        if i != -1 and i > last[0]:
            last[0] = i
            last[1] = nums.index(num)

    for char in line[:first[0]]:
        if char.isdigit():
            first[1] = int(char)
            break

    for i, char in enumerate(line[last[0]:][::-1]):
        if char.isdigit():
            last[1] = int(char)
            break

    result += first[1] * 10 + last[1]
print(result)
