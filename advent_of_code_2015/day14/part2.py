with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

import re

reindeers = {}
for reinder in data:
    result = re.search('(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', reinder)
    reindeers[result.group(1)] = [int(result.group(2)), int(result.group(3)), int(result.group(4)), [], 0]


answer = float('-inf')
for reinder in reindeers:
    resting_for = 0
    rest_in = reindeers[reinder][1]
    traveled_distance = 0
    for _ in range(2503):
        if resting_for > 0:
            resting_for -= 1

        elif rest_in == 0:
            resting_for = reindeers[reinder][2] - 1
            rest_in = reindeers[reinder][1]

        else:
            traveled_distance += reindeers[reinder][0]
            rest_in -= 1

        reindeers[reinder][3].append(traveled_distance)
    # print(reindeers[reinder][3])


for i in range(2503):
    furthest_distance = 0
    for reinder in reindeers:
        if reindeers[reinder][3][i] > furthest_distance:
            furthest_distance = reindeers[reinder][3][i]

    for reinder in reindeers:
        if reindeers[reinder][3][i] == furthest_distance:
            reindeers[reinder][4] += 1


answer = 0
for reinder in reindeers:
    if reindeers[reinder][4] > answer:
        answer = reindeers[reinder][4]

for reinder in reindeers:
    if reindeers[reinder][4] == answer:
        print(f'Winner is {reinder} with {answer} points')
        break
