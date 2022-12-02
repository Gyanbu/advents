with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

import re


ingredients = []
for ingredient in data:
    r = re.search('(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', ingredient)
    ingredients.append([int(r.group(2)), int(r.group(3)), int(r.group(4)), int(r.group(5)), int(r.group(6))])
# print(ingredients)

highest_score = 0
for q in range(101):
    for x in range(101 - q):
        for y in range(101 - q - x):
            z = 100 - q - x - y
            combination = [q, x, y, z]

            capacity = 0
            durability = 0
            flavor = 0
            texture = 0
            # calories = 0
            for i, ingredient in enumerate(ingredients):
                capacity += combination[i] * ingredient[0]
                durability += combination[i] * ingredient[1]
                flavor += combination[i] * ingredient[2]
                texture += combination[i] * ingredient[3]
                # calories += combination[i] * ingredient[4]
            if capacity > 0 and durability > 0 and flavor > 0 and texture > 0: # and calories > 0:
                score = capacity * durability * flavor * texture # * calories
                if score > highest_score:
                    highest_score = score
                    # print(combination)
print(highest_score)