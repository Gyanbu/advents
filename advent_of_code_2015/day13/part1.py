with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

import re

guests = []
relations = {}
for relation in data:
    result = re.search('(.*) would (?:lose|gain) (\d+) happiness units by sitting next to (.*).', relation)

    if not result.group(1) in guests:
        guests.append(result.group(1))
    if not result.group(3) in guests:
        guests.append(result.group(3))

    if not result.group(1) in relations:
        relations[result.group(1)] = {}
    if 'gain' in relation:
        relations[result.group(1)][result.group(3)] = int(result.group(2))
    else:
        relations[result.group(1)][result.group(3)] = -int(result.group(2))
del data, result, relation


def recurse_neighbors(neighbors, parsed_neighbors):
    if len(parsed_neighbors) == len(neighbors):
        try:
            # for i in range(len(parsed_neighbors)):
            #     parsed_neighbors.append(parsed_neighbors.pop(0))
            #     if parsed_neighbors in recurse_neighbors.results or parsed_neighbors[::-1] in recurse_neighbors.results:
            #         return
            recurse_neighbors.results.append(parsed_neighbors)
        except AttributeError:
            recurse_neighbors.results = [parsed_neighbors]

    for neighbor in neighbors:
        if neighbor not in parsed_neighbors:
            seated_guests_copy = parsed_neighbors.copy()
            seated_guests_copy.append(neighbor)
            recurse_neighbors(neighbors, seated_guests_copy)
    return recurse_neighbors.results


def calculate_happiness(guest_order):
    happiness = 0
    for i, guest in enumerate(guest_order):
        # print(f'{guest_order = }\n{i} -> {guest}\n')
        if i == 0:
            happiness += relations[guest][guest_order[-1]]
            happiness += relations[guest][guest_order[i+1]]
        elif i == len(guest_order) - 1:
            happiness += relations[guest][guest_order[i-1]]
            happiness += relations[guest][guest_order[0]]
        else:
            happiness += relations[guest][guest_order[i - 1]]
            happiness += relations[guest][guest_order[i + 1]]
    return happiness


guest_combinations = recurse_neighbors(guests, [])


answer = float('-inf')
for combination in guest_combinations:
    happiness = calculate_happiness(combination)
    if happiness > answer:
        answer = happiness
print(f'{answer = }')