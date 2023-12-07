total = 0

with open('day_04.txt') as f:
	for line in f:
		lists = line[(line.index(':') + 1):].rstrip().split('|')
		winning = set([number.strip() for number in lists[0].split(' ') if len(number) > 0])
		matches = 0

		for number in lists[1].split(' '):
			if number.strip() in winning:
				matches += 1

		if matches > 0:
			total += pow(2, matches - 1)

print(total)
