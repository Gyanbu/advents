import string
from functools import cache

# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)

with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
    # data = f.readlines()
print(data)


alphabet = string.ascii_letters
print(alphabet)

