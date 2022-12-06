with open('data.txt', 'rt') as f:
    data = f.readline().strip()
    # data = f.readlines()
print(data)
# data = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  # 11


def is_marker(string):
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True


seq_len = 4
for i in range((len(data) - seq_len + 1)):
    buf = data[i:i+seq_len]

    if is_marker(buf):
        print(i + seq_len)
        break

