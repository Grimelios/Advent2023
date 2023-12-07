total = 0

with open('day_02.txt') as f:
	results = {
		'red': 0,
		'green': 0,
		'blue': 0
	}

	for i, line in enumerate(f):
		results['red'] = 0
		results['green'] = 0
		results['blue'] = 0
		rounds = line[(line.index(':') + 1):].split(';')

		for cube_round in rounds:
			draws = cube_round.split(',')

			for draw in draws:
				tokens = draw.strip().split(' ')
				count = int(tokens[0])
				color = tokens[1]
				results[color] = max(count, results[color])

		power = results['red'] * results['green'] * results['blue']
		total += power

print(total)
