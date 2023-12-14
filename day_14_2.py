def cycle(grid):
	for j in range(4):
		slide(grid)

		grid = rotate(grid)

	return grid

def rotate(grid):
	w = len(grid[0])
	h = len(grid)
	rotated = []

	for i in range(h):
		rotated.append(['.'] * w)

	for y in range(h):
		for x in range(w):
			rotated[x][w - y - 1] = grid[y][x]

	return rotated

def slide(grid):
	w = len(grid[0])
	h = len(grid)

	for x in range(w):
		y = 0
		dots = 0

		while y < h:
			match grid[y][x]:
				case '.':
					dots += 1

				case 'O':
					if dots > 0:
						grid[y - dots][x] = 'O'
						grid[y][x] = '.'

				case '#':
					dots = 0

			y += 1

def stringify(grid):
	w = len(grid[0])
	h = len(grid)
	builder = [' '] * (w * h)

	for y in range(h):
		for x in range(w):
			builder[y * w + x] = grid[y][x]

	return ''.join(builder)


def weigh(grid):
	w = len(grid[0])
	h = len(grid)
	weight = 0

	for x in range(w):
		for y in range(h):
			if grid[y][x] == 'O':
				weight += h - y

	return weight

grid = []

with open('day_14.txt') as f:
	for line in f:
		grid.append([c for c in line.rstrip()])

cache = {}
order = []
cycles = 1000000000

for i in range(cycles):
	key = stringify(grid)

	if key in cache:
		offset = cache[key][0]
		loop = i - offset
		leftover = (cycles - offset) % loop
		key = order[offset + leftover]

		print(cache[key][1])

		break

	weight = weigh(grid)
	cache[key] = (i, weight)
	order.append(key)
	grid = cycle(grid)
