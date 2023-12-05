with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

seeds = [int(num) for num in data[0].split()[1:]]
print(seeds)

data = data[3:]
maps = []
map_buf = {}
for line in data:
    if len(line.split()) == 2:
        # print(line.split()[0])
        maps.append(map_buf)
        map_buf = {}

    elif len(line.split()) == 3:
        nums = [int(num) for num in line.split()]
        map_buf[nums[1]] = (nums[0], nums[2])
maps.append(map_buf)


for s, seed in enumerate(seeds):
    for map_instruction in maps:
        print(seed, end='->')
        for num in sorted(map_instruction.keys(), reverse=True):
            if seed >= num and seed <= num + map_instruction[num][1] - 1:
                # print(f'{seed}: {num} {map_instruction[num][0]} {map_instruction[num][1]}')
                shift = map_instruction[num][0] - num
                seed += shift
                break
    seeds[s] = seed
    print(seed)
print(sorted(seeds)[0])
