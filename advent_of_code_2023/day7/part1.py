with open('data.txt', 'rt') as f:
# with open('test_data.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

face_cards = {
    'T': 10,
    'J': 11,
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
    for card in hand:
        if not cards.get(card):
            cards[card] = 1
        else:
            cards[card] += 1
    # print(cards)

    if 5 in cards.values():
        # Five of a kind
        return 6
    elif 4 in cards.values():
        # Four of a kind
        return 5
    elif 3 in cards.values() and 2 in cards.values():
        # Full house
        return 4
    elif 3 in cards.values():
        # Three of a kind
        return 3
    elif list(cards.values()).count(2) == 2:
        # Two pair
        return 2
    elif 2 in cards.values():
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
