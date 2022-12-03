import string

# with open('data.txt', 'rt') as f:
#     data = [line.strip() for line in f.readlines()]
#     # data = f.readlines()
# print(data)
data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']  # 18


alphabet = string.ascii_letters
bags = []
for bag in data:
    buf = []
    for letter in bag[:len(bag) // 2]:
        buf.append(alphabet.index(letter))
    for letter in bag[len(bag) // 2:]:
        buf.append(alphabet.index(letter))
    bags.append(buf)


answer = 0
for elf_group in range(len(bags) // 3):
    elf_group = bags[elf_group * 3:elf_group * 3 + 3]
    for item in elf_group[0]:
        if item in elf_group[1] and item in elf_group[2]:
            answer += item + 1
            break
print(answer)
