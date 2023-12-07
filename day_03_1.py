with open('day_03.txt') as f:
	symbols = set()

	for y, line in enumerate(f):
		for x, c in enumerate(line.rstrip()):
			if not c.isdigit() and c != '.':
				symbols.add((x, y))

total = 0

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

			for coords in check:
				if coords in symbols:
					total += int(''.join(digits))

					break

		y += 1

print(total)
