all_matches = []

with open('day_04.txt') as f:
	for line in f:
		lists = line[(line.index(':') + 1):].rstrip().split('|')
		winning = set([number.strip() for number in lists[0].split(' ') if len(number) > 0])
		matches = 0

		for number in lists[1].split(' '):
			if number.strip() in winning:
				matches += 1

		all_matches.append(matches)

copies = [1] * len(all_matches)

for i, matches in enumerate(all_matches):
	for j in range(matches):
		copies[i + j + 1] += copies[i]

print(sum(copies))
