rows = []

with open('day_14.txt') as f:
	for line in f:
		rows.append([c for c in line.rstrip()])

w = len(rows[0])
h = len(rows)

for x in range(w):
	y = 0
	dots = 0

	while y < h:
		match rows[y][x]:
			case '.':
				dots += 1

			case 'O':
				if dots > 0:
					rows[y - dots][x] = 'O'
					rows[y][x] = '.'

			case '#':
				dots = 0

		y += 1

total = 0

for x in range(w):
	for y in range(h):
		if rows[y][x] == 'O':
			total += h - y

print(total)
