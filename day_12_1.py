def is_satisfied(row, counts):
	parts = []
	i = 0

	while i < len(row):
		current = 0

		while i < len(row) and row[i] == '#':
			current += 1
			i += 1

		if current > 0:
			parts.append(current)

		i += 1

	if len(parts) != len(counts):
		return False

	for i, part in enumerate(parts):
		if counts[i] != part:
			return False

	return True

def recurse(row, counts, index):
	if index == len(row):
		return 1 if is_satisfied(row, counts) else 0

	if row[index] != '?':
		return recurse(row, counts, index + 1)

	total = 0
	row[index] = '.'
	total += recurse(row, counts, index + 1)
	row[index] = '#'
	total += recurse(row, counts, index + 1)
	row[index] = '?'
	
	return total

with open('day_12.txt') as f:
	rows = []
	contiguous = []

	for line in f:
		parts = line.rstrip().split(' ')
		rows.append([c for c in parts[0]])
		contiguous.append([int(c) for c in parts[1].split(',')])

total = 0

for i, row in enumerate(rows):
	total += recurse(row, contiguous[i], 0)

print(total)
