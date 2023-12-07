with open('day_03.txt') as f:
	symbols = set()
	gears = set()

	for y, line in enumerate(f):
		for x, c in enumerate(line.rstrip()):
			if not c.isdigit() and c != '.':
				symbols.add((x, y))

				if c == '*':
					gears.add((x, y))

gear_adjacency = {}

with open('day_03.txt') as f:
	for y, line in enumerate(f):
		width = len(line.rstrip())
		x = 0

		while x < width:
			current = line[x]
			x += 1

			if not current.isdigit():
				continue

			digits = [current]
			left = x - 2
			top = y - 1
			bottom = y + 1

			while x < width:
				c = line[x]

				if not c.isdigit():
					break

				digits.append(c)
				x += 1

			right = x
			w_local = right - left + 1
			h_local = bottom - top
			check = [(left, y), (right,  y)]

			for x_local in range(w_local):
				check.append((left + x_local, top))
				check.append((left + x_local, bottom))

			is_part = False

			for coords in check:
				if coords in symbols:
					part = int(''.join(digits))

					if coords in gears:
						gear_adjacency.setdefault((coords), []).append(part)

		y += 1

total = 0

for gear, numbers in gear_adjacency.items():
	if len(numbers) != 2:
		continue

	gear_ratio = numbers[0] * numbers[1]
	total += gear_ratio

print(total)
