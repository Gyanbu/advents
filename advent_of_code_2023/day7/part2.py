with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

face_cards = {
    'T': 10,
    'J': 0,
    'Q': 12,
    'K': 13,
    'A': 14
}
rank = len(data)

print(data)
for g, game in enumerate(data):
    game = game.split()

    buf = []
    for card in game[0]:
        if card.isdigit():
            buf.append(int(card))
        else:
            buf.append(face_cards[card])

    data[g] = [buf, int(game[1])]
# print(data)


def hand_type(hand):
    cards = {}
    jokers = 0
    for card in hand:
        if card == 0:
            jokers += 1
        elif not cards.get(card):
            cards[card] = 1
        else:
            cards[card] += 1

    # for card_type in cards.keys():
    #     cards[card_type] += jokers
    # print(cards)

    if 5 - jokers in cards.values() or jokers == 5:
        # Five of a kind
        return 6
    elif 4 - jokers in cards.values() or (3 in cards.values() and jokers == 1):
        # Four of a kind
        return 5
    elif 3 in cards.values() and 2 in cards.values() or ((3 in cards.values() or list(cards.values()).count(2) == 2) and jokers == 1):
        # Full house
        return 4
    elif 3 in cards.values() or (2 in cards.values() and jokers == 1) or jokers == 2:
        # Three of a kind
        return 3
    elif list(cards.values()).count(2) == 2:
        # Two pair
        return 2
    elif 2 in cards.values() or jokers == 1:
        # Pair
        return 1
    else:
        # High card
        return 0


buf = {6: [], 5: [], 4: [], 3: [], 2: [], 1: [], 0: []}
for h, hand in enumerate(data):
    buf[hand_type(hand[0])].append(hand)
data = buf
print(data)

result = 0
for i in range(len(data) - 1, -1, -1):
    for hand in sorted(data[i], reverse=True):
        result += hand[1] * rank
        rank -= 1
print(result)
