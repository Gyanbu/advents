with open('data.txt', 'rt') as f:
    data = [int(line.strip()) for line in f.readlines()]

data = sorted(data)[::-1]
eggnog = 150


def recurse_budyn(containers, liters, used_containers=None, most_containers=[float('inf'), 0]):
    if used_containers is None:
        used_containers = []
    if liters == 0:
        filled_containers = 0
        for tuple in used_containers:
            if tuple[1]:
                filled_containers += 1

        if filled_containers == most_containers[0]:
            most_containers[1] += 1
        elif filled_containers < most_containers[0]:
            most_containers = [filled_containers, 1]
        return most_containers
    elif len(containers) == 0:
        return most_containers

    containers_cp = containers.copy()
    container = containers_cp.pop(0)
    # used_containers.append(container)
    if liters - container >= 0:
        most_containers = recurse_budyn(containers_cp, liters - container, used_containers + [(container, True)], most_containers)
    most_containers = recurse_budyn(containers_cp, liters, used_containers + [(container, False)], most_containers)
    return most_containers


result = recurse_budyn(data, eggnog)
print(result)
