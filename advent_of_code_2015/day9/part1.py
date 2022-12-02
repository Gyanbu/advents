with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]


import re
connections_dict = {}
cities_dict = {}
for line in data:
    result = re.search('(.*) to (.*) = (.*)', line)
    if result.group(1) not in connections_dict:
        connections_dict[result.group(1)] = []
        cities_dict[result.group(1)] = True
    if result.group(2) not in connections_dict:
        connections_dict[result.group(2)] = []
        cities_dict[result.group(2)] = True
    connections_dict[result.group(1)].append((result.group(2), int(result.group(3))))
    connections_dict[result.group(2)].append((result.group(1), int(result.group(3))))


def shortest_path(city, visited_cities, traveled_distance):
    if len(visited_cities) == len(cities_dict.keys()):
        global answer
        if answer[0] > traveled_distance:
            print(f'{" -> ".join(visited_cities)} = {traveled_distance}')
            answer[0] = traveled_distance
            answer[1] = ' -> '.join(visited_cities)
        return traveled_distance
    directions = connections_dict[city]
    # print(directions)
    for direction, distance in directions:
        if direction not in visited_cities:
            new_visited_cities = visited_cities.copy()
            new_visited_cities.append(direction)
            shortest_path(direction, new_visited_cities, traveled_distance + distance)
    return traveled_distance


answer = [9999999999, '']
for city in connections_dict.keys():
    visited_cities = [city]
    shortest_path(city, visited_cities, 0)

print(answer)
