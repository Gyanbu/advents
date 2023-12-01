with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
# print(data[:4])

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for l in range(len(data)):
    buf = ''
    for char in data[l]:
        buf += char
        for i in range(len(nums)):
            while True:
                if (j := buf.find(nums[i])) != -1:
                    buf = buf[:j] + str(i) + buf[j + len(nums[i]):]
                    continue
                break
    data[l] = buf


def first_and_last_number(line):
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

    return first * 10 + last


result = 0
for line in data:
    result += first_and_last_number(line)
print(result)
