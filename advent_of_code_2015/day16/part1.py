with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

sues = {}
for i, sue in enumerate(data):
    sues[i+1] = {}
    sue = sue.split()
    attr = ''
    for j, group in enumerate(sue[2:]):
        if j % 2: # odd
            sues[i+1][attr] = int(group.strip(','))
        else: # even
            attr = group.strip(':')


best_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


for sue in sues:
    wrong_sue = False
    for attr in sues[sue]:
        if sues[sue][attr] != best_sue[attr]:
            wrong_sue = True
            break
    if not wrong_sue:
        print(sue)
