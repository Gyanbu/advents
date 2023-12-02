with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]
r, g, b = 12, 13, 14

parsed_data = []
for game in data:
    buf = {}
    game_id, game = game.split(': ')
    buf['id'] = int(game_id.split(' ')[1])
    game = game.split('; ')
    buf['rounds'] = []
    for round in game:
        round = round.split(', ')
        rgb = [0, 0, 0]
        for cubes in round:
            cubes = cubes.split(' ')
            if cubes[1] == 'red':
                rgb[0] += int(cubes[0])
            elif cubes[1] == 'green':
                rgb[1] += int(cubes[0])
            elif cubes[1] == 'blue':
                rgb[2] += int(cubes[0])
        buf['rounds'].append(tuple(rgb))
    parsed_data.append(buf)
print(parsed_data)

answer = 0
for game in parsed_data:
    skip = False
    for round in game['rounds']:
        if round[0] > r or round[1] > g or round[2] > b:
            skip = True
            break
    if skip:
        continue
    answer += game['id']
print(answer)
