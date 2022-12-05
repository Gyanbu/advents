from copy import deepcopy


boss = {
    'health': 103,
    'damage': 9,
    'armor':  2
}

player = {
    'health': 100,
    'damage': 0,
    'armor':  0,
    'cost': 0
}

weapons = {
    'dagger':     [8, 4, 0],
    'shortsword': [10, 5, 0],
    'warhammer':  [25, 6, 0],
    'longsword':  [40, 7, 0],
    'greataxe':   [74, 8, 0]
}

armors = {
    'none':       [0, 0, 0],
    'leather':    [12, 0, 1],
    'chainmail':  [31, 0, 2],
    'splintmain': [53, 0, 3],
    'bandedmail': [75, 0, 4],
    'platemail':  [102, 0, 5]
}

rings = {
    'none': [0, 'armor', 0],
    'dmg1': [25, 'damage', 1],
    'dmg2': [50, 'damage', 2],
    'dmg3': [100, 'damage', 3],
    'def1': [20, 'armor', 1],
    'def2': [40, 'armor', 2],
    'def3': [80, 'armor', 3]
}


def print_info(entity, name):
    print(f'[{name}]\nhealth: {entity["health"]}\ndamage: {entity["damage"]}\narmor:  {entity["armor"]}')


def fight_tick(player, boss):
    damage = player['damage'] - boss['armor']
    if damage < 1:
        damage = 1
    boss['health'] -= damage
    # print_info(boss, 'boss')
    if boss['health'] <= 0:
        return

    damage = boss['damage'] - player['armor']
    if damage < 1:
        damage = 1
    player['health'] -= damage
    # print_info(player, 'player')


def fight(player, boss):
    player_cpy = deepcopy(player)
    boss_cpy = deepcopy(boss)
    # print_info(boss, 'boss')
    # print_info(player, 'player')
    while True:
        # print()
        fight_tick(player_cpy, boss_cpy)
        if boss_cpy['health'] <= 0:
            # print('Player won!')
            return True
        if player_cpy['health'] <= 0:
            # print('Player was defeated!')
            return False


lowest_budget = float('-inf')
for weapon in weapons.values():
    player_cpy = deepcopy(player)
    player_cpy['damage'] += weapon[1]
    player_cpy['cost'] += weapon[0]

    for armor in armors.values():
        player_cpy2 = deepcopy(player_cpy)
        player_cpy2['armor'] += armor[2]
        player_cpy2['cost'] += armor[0]

        for ring in rings.values():
            player_cpy3 = deepcopy(player_cpy2)
            player_cpy3['ring'] = ring
            player_cpy3[ring[1]] += ring[2]
            player_cpy3['cost'] += ring[0]

            for ring2 in rings.values():
                player_cpy4 = deepcopy(player_cpy3)
                if player_cpy3['ring'] != ring2:
                    player_cpy4[ring2[1]] += ring2[2]
                    player_cpy4['cost'] += ring2[0]
                    # print(player_cpy4)
                if player_cpy4['cost'] > lowest_budget and not fight(player_cpy4, boss):
                    print(player_cpy4['cost'])
                    lowest_budget = player_cpy4['cost']
print(lowest_budget)
