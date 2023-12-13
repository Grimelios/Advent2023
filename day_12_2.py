def recurse(row, row_start, counts, count_start, accumulated, limit, lookup):
	i = row_start
	j = count_start
	key = (i, j, accumulated)

	if key in lookup:
		return lookup[key]

	if j == len(counts):
		while i < len(row):
			if row[i] == '#':
				lookup[key] = 0

				return 0

			i += 1

		lookup[key] = 1

		return 1

	required = counts[j]
	limit -= required - accumulated + 1
	remaining = len(row) - i
	comparison = remaining + required - accumulated - (1 if j < len(counts) - 1 else 0)

	if comparison < limit:
		lookup[key] = 0

		return 0

	if i >= len(row):
		lookup[key] = 0

		return 0

	if row[i] == '.':
		if accumulated > 0:
			lookup[key] = 0

			return 0

		while i < len(row) and row[i] == '.':
			i += 1

		if i == len(row):
			lookup[key] = 0

			return 0

	total = 0
	c = row[i]
	i += 1

	if c == '#':
		if accumulated < required - 1:
			total += recurse(row, i, counts, j, accumulated + 1, limit, lookup)
		else:
			if i < len(row) and row[i] == '#':
				lookup[key] = 0

				return 0

			total += recurse(row, i + 1, counts, j + 1, 0, limit - required - 1, lookup)
	else:
		if accumulated == 0:
			total += recurse(row, i, counts, j, 0, limit, lookup)

		if accumulated == required - 1:
			if i == len(row) or row[i] != '#':
				total += recurse(row, i + 1, counts, j + 1, 0, limit - required - 1, lookup)
		else:
			total += recurse(row, i, counts, j, accumulated + 1, limit, lookup)

	lookup[key] = total

	return total

with open('day_12.txt') as f:
	rows = []
	contiguous = []

	for line in f:
		parts = line.rstrip().split(' ')
		rows.append((''.join([parts[0] + '?'] * 5))[:-1])
		contiguous.append([int(c) for c in ','.join([parts[1]] * 5).split(',')])

total = 0

for i, row in enumerate(rows):
	counts = contiguous[i]
	limit = sum(counts) + len(counts) - 1
	total += recurse(row, 0, counts, 0, 0, limit, {})

print(total)
