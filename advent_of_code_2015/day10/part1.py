data = '1113122113'


def parse_conway_seq(data):
    digits_in_a_row = 1
    previous_digit = data[0]
    next_array = []
    for i, digit in enumerate(data):
        if i == 0:
            continue

        if digit != previous_digit:
            next_array.append(str(digits_in_a_row))
            next_array.append(str(previous_digit))
            digits_in_a_row = 1
            previous_digit = digit
        else:
            digits_in_a_row += 1

        if i + 1 == len(data):
            if digit != previous_digit:
                next_array.append('1')
                next_array.append(str(digit))
            else:
                # digits_in_a_row += 1
                next_array.append(str(digits_in_a_row))
                next_array.append(str(previous_digit))

    return ''.join(next_array)


# print(parse_conway_seq(data))

for _ in range(40):
    data = parse_conway_seq(data)
print(len(data))
