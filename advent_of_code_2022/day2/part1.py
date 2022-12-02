with open('data.txt', 'rt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]
# print(data)
# Rock:     A, X
# Paper:    B, Y
# Scissors: C, Z


for g, game in enumerate(data):
    for c, choice in enumerate(game):
        if choice == 'A' or choice == 'X':
            data[g][c] = 1
        elif choice == 'B' or choice == 'Y':
            data[g][c] = 2
        elif choice == 'C' or choice == 'Z':
            data[g][c] = 3
# print(data)
# Rock:     1
# Paper:    2
# Scissors: 3


total_score = 0
for game in data:
    total_score += game[1]  # Add user's choice

    if game[1] == 1:  # User choose rock
        if game[0] == 1:  # Enemy choose rock
            total_score += 3
        elif game[0] == 2:  # Enemy choose paper
            total_score += 0
        elif game[0] == 3:  # Enemy choose scissors
            total_score += 6
    elif game[1] == 2:  # User choose paper
        if game[0] == 1:  # Enemy choose rock
            total_score += 6
        elif game[0] == 2:  # Enemy choose paper
            total_score += 3
        elif game[0] == 3:  # Enemy choose scissors
            total_score += 0
    elif game[1] == 3:  # User choose scissors
        if game[0] == 1:  # Enemy choose rock
            total_score += 0
        elif game[0] == 2:  # Enemy choose paper
            total_score += 6
        elif game[0] == 3:  # Enemy choose scissors
            total_score += 3
print(total_score)
