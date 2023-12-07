total = 0

with open('day_02.txt') as f:
	results = {
		'red': 0,
		'green': 0,
		'blue': 0
	}

	for i, line in enumerate(f):
		rounds = line[(line.index(':') + 1):].split(';')
		possible = True

		for cube_round in rounds:
			results['red'] = 0
			results['green'] = 0
			results['blue'] = 0
			draws = cube_round.split(',')

			for draw in draws:
				tokens = draw.strip().split(' ')
				count = int(tokens[0])
				color = tokens[1]
				results[color] = count

			if results['red'] > 12 or results['green'] > 13 or results['blue'] > 14:
				possible = False

				break

		if possible:
			game = i + 1
			total += game

print(total)
