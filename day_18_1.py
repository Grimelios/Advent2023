path = [(0, 0)]
minimum = [0, 0]
maximum = [0, 0]

with open('day_18.txt') as f:
	coords = [0, 0]

	for line in f:
		parts = line.rstrip().split(' ')
		length = int(parts[1])
		v = [0, 0]

		match parts[0]:
			case 'D':
				v[1] = 1

			case 'L':
				v[0] = -1

			case 'R':
				v[0] = 1

			case 'U':
				v[1] = -1

		for i in range(length):
			coords[0] += v[0]
			coords[1] += v[1]
			minimum[0] = min(minimum[0], coords[0])
			minimum[1] = min(minimum[1], coords[1])
			maximum[0] = max(maximum[0], coords[0])
			maximum[1] = max(maximum[1], coords[1])
			path.append((coords[0], coords[1]))

w = (maximum[0] - minimum[0]) + 1
h = (maximum[1] - minimum[1]) + 1
grid = []

for i in range(h):
	grid.append(['.'] * w)

for e in path:
	x = e[0] - minimum[0]
	y = e[1] - minimum[1]
	grid[y][x] = '#'

stack = [(142, 1)]
filled = set()

while len(stack) > 0:
	current = stack.pop()
	x, y = current

	if current in filled or grid[y][x] == '#':
		continue

	filled.add(current)
	stack.append((x + 1, y))
	stack.append((x - 1, y))
	stack.append((x, y + 1))
	stack.append((x, y - 1))

dug = len(path) + len(filled) - 1

print(dug)
