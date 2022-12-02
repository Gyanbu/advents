with open('data.txt', 'rt') as f:
    data = [int(line.strip()) for line in f.readlines()]

data = sorted(data)[::-1]
eggnog = 150


def recurse_budyn(containers, liters, used_containers=None, result=0):
    if used_containers is None:
        used_containers = []
    if liters == 0:
        # try:
        #     recurse_budyn.result += 1
        # except AttributeError:
        #     recurse_budyn.result = 1
        # finally:
        #     print(used_containers)
        return result + 1
    elif len(containers) == 0:
        return result

    containers_cp = containers.copy()
    container = containers_cp.pop(0)
    # used_containers.append(container)
    if liters - container >= 0:
        result += recurse_budyn(containers_cp, liters - container, used_containers + [(container, True)])
    result += recurse_budyn(containers_cp, liters, used_containers + [(container, False)])
    return result


result = recurse_budyn(data, eggnog)
print(result)
