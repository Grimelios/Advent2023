def recurse(row, row_start, counts, count_start, accumulated, limit):
	i = row_start
	j = count_start

	if j == len(counts):
		while i < len(row):
			if row[i] == '#':
				return 0

			i += 1

		return 1

	required = counts[j]
	limit -= required - accumulated + 1
	remaining = len(row) - i
	comparison = remaining + required - accumulated - (1 if j < len(counts) - 1 else 0)

	if comparison < limit:
		return 0

	if i >= len(row):
		return 0

	if row[i] == '.':
		if accumulated > 0:
			return 0

		while i < len(row) and row[i] == '.':
			i += 1

		if i == len(row):
			return 0

	total = 0
	c = row[i]
	i += 1

	if c == '#':
		if accumulated < required - 1:
			total += recurse(row, i, counts, j, accumulated + 1, limit)
		else:
			if i < len(row) and row[i] == '#':
				return 0

			total += recurse(row, i + 1, counts, j + 1, 0, limit - required - 1)
	else:
		if accumulated == 0:
			total += recurse(row, i, counts, j, 0, limit)

		if accumulated == required - 1:
			if i == len(row) or row[i] != '#':
				total += recurse(row, i + 1, counts, j + 1, 0, limit - required - 1)
		else:
			total += recurse(row, i, counts, j, accumulated + 1, limit)

	return total

with open('day_12.txt') as f:
	rows = []
	contiguous = []

	for line in f:
		parts = line.rstrip().split(' ')
		rows.append((''.join([parts[0] + '?'] * 5))[:-1])
		contiguous.append([int(c) for c in ','.join([parts[1]] * 5).split(',')])

test = False

if test:
	index = 10
	row = rows[index]
	counts = contiguous[index]
	limit = sum(counts) + len(counts) - 1
	total = recurse(row, 0, counts, 0, 0, limit)

	print(f'{row} -> {total}')
	quit()

total = 0

for i, row in enumerate(rows):
	counts = contiguous[i]
	limit = sum(counts) + len(counts) - 1
	original = total
	total += recurse(row, 0, counts, 0, 0, limit)

	print(f'{i + 1}. {row} -> {total - original}')

print(total)
