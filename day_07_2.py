from functools import cmp_to_key

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
HIGH_CARD = 0
CARDS = {
	'A': 13,
	'K': 12,
	'Q': 11,
	'T': 10,
	'9': 9,
	'8': 8,
	'7': 7,
	'6': 6,
	'5': 5,
	'4': 4,
	'3': 3,
	'2': 2,
	'J': 1
}

ONE_PAIR = 1
THREE_OF_A_KIND = 3
TWO_PAIR = 2

def compare(a, b):
	t_a = a[1]
	t_b = b[1]

	if t_a != t_b:
		return 1 if t_a > t_b else -1

	hand_a = a[0]
	hand_b = b[0]

	for i in range(5):
		card_a = hand_a[i]
		card_b = hand_b[i]

		if card_a == card_b:
			continue

		value_a = CARDS[card_a]
		value_b = CARDS[card_b]

		return 1 if value_a > value_b else -1

	return 0

def compute(hand):
	counts = {}

	for card in hand:
		counts.setdefault(card, 0)
		counts[card] += 1

	unique = len(counts)

	if 'J' in counts:
		j_count = counts['J']

		if j_count >= 4:
			return FIVE_OF_A_KIND

		if j_count == 3:
			return FIVE_OF_A_KIND if unique == 2 else FOUR_OF_A_KIND

		hand_sorted = sorted(hand)

		if j_count == 2:
			if unique == 2:
				return FIVE_OF_A_KIND

			return FOUR_OF_A_KIND if unique == 3 else THREE_OF_A_KIND

		if unique == 2:
			return FIVE_OF_A_KIND

		if unique == 3:
			return FULL_HOUSE if any([count == 2 for count in counts.values()]) else FOUR_OF_A_KIND

		return THREE_OF_A_KIND if unique == 4 else ONE_PAIR

	if unique == 1:
		return FIVE_OF_A_KIND

	if unique == 2:
		hand_sorted = sorted(hand)
		instances_of_first = 1

		for i in range(3):
			if hand_sorted[0] != hand_sorted[i + 1]:
				break

			instances_of_first += 1

		return FOUR_OF_A_KIND if instances_of_first == 1 or instances_of_first == 4 else FULL_HOUSE

	if unique == 3:
		return THREE_OF_A_KIND if any([count == 3 for count in counts.values()]) else TWO_PAIR

	return ONE_PAIR if unique == 4 else HIGH_CARD

hands = []

with open('day_07.txt') as f:
	for line in f:
		parts = line.rstrip().split(' ')
		hand = parts[0]
		bid = int(parts[1])
		t = compute(hand)
		hands.append((hand, t, bid))

hands.sort(key = cmp_to_key(compare))
winnings = 0

for i, triple in enumerate(hands):
	winnings += (i + 1) * triple[2]

print(winnings)
