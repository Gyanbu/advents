import json
data = json.load(open('data.txt', 'rt'))


def sum_of_numbers(obj):
    obj_sum = 0
    if isinstance(obj, dict):
        for item in obj.items():
            obj_sum += sum_of_numbers(item)

    if isinstance(obj, list) or isinstance(obj, tuple):
        for item in obj:
            obj_sum += sum_of_numbers(item)

    if isinstance(obj, int):
        obj_sum += obj

    return obj_sum


print(sum_of_numbers(data))
