with open('day_11.txt') as f:
	rows = [line.rstrip() for line in f]

expanded_rows = set()
expanded_columns = set()

for y, row in enumerate(rows):
	if all([c == '.' for c in row]):
		expanded_rows.add(y)

for x in range(len(rows[0])):
	all_dots = True

	for y, row in enumerate(rows):
		if row[x] == '#':
			all_dots = False

			break

	if all_dots:
		expanded_columns.add(x)

galaxies = []
y_expansion = 0

for y, row in enumerate(rows):
	if y in expanded_rows:
		y_expansion += 999999

		continue

	x_expansion = 0

	for x, c in enumerate(row):
		if x in expanded_columns:
			x_expansion += 999999

			continue

		if c == '#':
			galaxies.append((x + x_expansion, y + y_expansion))

total = 0

for i in range(len(galaxies)):
	a = galaxies[i]
	j = i + 1

	while j < len(galaxies):
		b = galaxies[j]
		j += 1
		delta_x = abs(a[0] - b[0])
		delta_y = abs(a[1] - b[1])
		manhattan = delta_x + delta_y
		total += manhattan

print(total)
