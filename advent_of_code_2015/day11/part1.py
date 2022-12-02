password_to_check = 'vzbxkghb'

alphabet = [char for char in 'abcdefghjkmnpqrstuvwxyz']


def next_password(password):
    password = [alphabet.index(char) for char in password]
    password = password[::-1]

    for i, char in enumerate(password):
        if char == 22: # Z
            password[i] = 0
        else:
            password[i] += 1
            break

    return ''.join([alphabet[char] for char in reversed(password)])


def check_pass(password):
    password = [alphabet.index(char) for char in password]

    pairs = {}
    pairs_cooldown = False
    three_in_a_row = False
    for i, char in enumerate(password):
        if i == 0:
            continue

        if pairs_cooldown:
            pairs_cooldown = False
        elif password[i-1] == char:
            pairs[char] = True
            pairs_cooldown = True

        if i == 1:
            continue

        if password[i-2]+2 == password[i-1]+1 == char:
            three_in_a_row = True

    if len(pairs) >= 2 and three_in_a_row:
        return True
    else:
        return False


while True:
    password_to_check = next_password(password_to_check)
    if check_pass(password_to_check):
        break
print(password_to_check)
