with open('data.txt', 'rt') as f:
    data = []
    line = f.readline().strip()
    while line:
        data.append(line)
        line = f.readline().strip()
    molecule = f.readline().strip()

buffer = ''
molecule_list = []
for letter in molecule:
    if letter.isupper():
        if buffer:
            molecule_list.append(buffer)
            buffer = ''
        buffer += letter
        continue
    else:
        molecule_list.append(buffer + letter)
        buffer = ''
# print(''.join(molecule_list) == molecule)


reactions = {}
for reaction in data:
    reaction = reaction.split(' => ')
    if reaction[0] in reactions.keys():
        reactions[reaction[0]].append(reaction[1])
    else:
        reactions[reaction[0]] = [reaction[1]]
# print(reactions)


molecules = []
for i, molecule in enumerate(molecule_list):
    if molecule not in reactions.keys():
        continue

    molecule_list_cp = molecule_list.copy()
    for reaction in reactions[molecule]:
        molecule_list_cp[i] = reaction
        if ''.join(molecule_list_cp) not in molecules:
            molecules.append(''.join(molecule_list_cp))


shortest_molecule = float('inf')
for molecule in molecules:
    if len(molecule) < shortest_molecule:
        shortest_molecule = len(molecule)
print(shortest_molecule)
print(len(''.join(molecule_list)))
