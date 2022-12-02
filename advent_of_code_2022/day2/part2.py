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
# Rock, lose:    1
# Paper, draw:   2
# Scissors, win: 3


total_score = 0
for game in data:
    # total_score += game[1]  # Add user's choice

    if game[0] == 1:  # Enemy choose rock
        if game[1] == 1:  # User loses
            total_score += 0 + 3
        elif game[1] == 2:  # User draws
            total_score += 3 + 1
        elif game[1] == 3:  # User wins
            total_score += 6 + 2
    if game[0] == 2:  # Enemy choose paper
        if game[1] == 1:  # User loses
            total_score += 0 + 1
        elif game[1] == 2:  # User draws
            total_score += 3 + 2
        elif game[1] == 3:  # User wins
            total_score += 6 + 3
    if game[0] == 3:  # Enemy choose scissors
        if game[1] == 1:  # User loses
            total_score += 0 + 2
        elif game[1] == 2:  # User draws
            total_score += 3 + 3
        elif game[1] == 3:  # User wins
            total_score += 6 + 1
print(total_score)
