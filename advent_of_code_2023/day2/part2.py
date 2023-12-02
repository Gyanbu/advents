with open('data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

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
    r, g, b = 0, 0, 0
    for round in game['rounds']:
        if round[0] > r:
            r = round[0]
        if round[1] > g:
            g = round[1]
        if round[2] > b:
            b = round[2]
    answer += r*g*b
print(answer)
