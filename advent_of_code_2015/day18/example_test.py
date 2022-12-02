with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]


from copy import deepcopy
grid = []
for _ in range(len(data)):
    grid.append([False] * len(data))

for i, line in enumerate(data):
    for j, light in enumerate(line):
        if light == '#':
            grid[i][j] = True


def get_alive_neighbors(grid, x, y):
    neighbors = 0
    if x > 0 and y > 0 and grid[y - 1][x - 1]:  # Upper left
        neighbors += 1
    if y > 0 and grid[y - 1][x]:  # Up
        neighbors += 1
    if x < len(grid) - 1 and y > 0 and grid[y - 1][x + 1]:  # Upper right
        neighbors += 1
    if x > 0 and grid[y][x - 1]:  # Left
        neighbors += 1
    if x < len(grid) - 1 and grid[y][x + 1]:  # Right
        neighbors += 1
    if x > 0 and y < len(grid) - 1 and grid[y + 1][x - 1]:  # Bottom left
        neighbors += 1
    if y < len(grid) - 1 and grid[y + 1][x]:  # Bottom
        neighbors += 1
    if x < len(grid) - 1 and y < len(grid) - 1 and grid[y + 1][x + 1]:  # Bottom right
        neighbors += 1
    return neighbors


def print_grid(grid):
    print()
    for line in grid:
        for light in line:
            if light:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()


def life_step(grid):
    grid_cp = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid)):
            alive_neighbors = get_alive_neighbors(grid, x, y)
            if grid[y][x] and alive_neighbors in (2, 3):
                continue
            elif not grid[y][x] and alive_neighbors == 3:
                grid_cp[y][x] = True
            else:
                grid_cp[y][x] = False
    return grid_cp


print_grid(grid)
for _ in range(4):
    grid = life_step(grid)
    print_grid(grid)
