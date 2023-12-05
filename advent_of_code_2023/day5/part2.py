with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]


seeds = [int(num) for num in data[0].split()[1:]]
seed_ranges = []
for i in range(len(seeds)//2):
    seed_ranges.append((seeds[i*2], seeds[i*2+1]))
seed_ranges = sorted(seed_ranges, key=lambda x: x[0], reverse=True)
print(seed_ranges)

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
        map_buf[nums[0]] = (nums[1], nums[2])
maps.append(map_buf)
maps = maps[::-1]


s = 0
while True:
    seed = s
    s += 1
    print(seed, end='<--')
    for map_instruction in maps:
        for num in sorted(map_instruction.keys()):
            if seed < num:
                break
            elif seed >= num and seed <= num + map_instruction[num][1] - 1:
                shift = num - map_instruction[num][0]
                seed -= shift
                break
    print(seed)
    for index, length in seed_ranges:
        if index <= seed < index + length:
            print(seed)
            exit()
