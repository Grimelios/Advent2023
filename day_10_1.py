CONNECTS_DOWN = set(['|', 'F', '7'])
CONNECTS_LEFT = set(['-', 'J', '7'])
CONNECTS_RIGHT = set(['-', 'F', 'L'])
CONNECTS_UP = set(['|', 'L', 'J'])

def alter_direction(c, direction, coords, w, h):
	x = coords[0]
	y = coords[1]

	match c:
		case '|':
			if direction[0] != 0 or y == 0 or y == h - 1:
				return (0, 0)

			if direction[1] == 0:
				direction = (0, 1)

		case '-':
			if direction == (0, 0) or direction[1] != 0 or x == 0 or x == w - 1:
				return (0, 0)

		case 'L':
			if direction[0] == 1 or direction[1] == -1 or y == 0 or x == w - 1:
				return (0, 0)

			if direction == (0, 0):
				direction = (1, 0)
			else:
				direction = (0, -1) if direction[0] == -1 else (1, 0)

		case 'J':
			if direction == (0, 0) or direction[0] == -1 or direction[1] == -1 or y == 0 or x == 0:
				return (0, 0)

			direction = (0, -1) if direction[0] == 1 else (-1, 0)

		case '7':
			if direction == (0, 0) or direction[0] == -1 or direction[1] == 1 or y == h - 1 or x == 0:
				return (0, 0)

			direction = (0, 1) if direction[0] == 1 else (-1, 0)

		case 'F':
			if direction[0] == 1 or direction[1] == 1 or y == h - 1 or x == w - 1:
				return (0, 0)

			if direction == (0, 0):
				direction = (0, 1)
			else:
				direction = (0, 1) if direction[0] == -1 else (1, 0)

	return direction

grid = []

with open('day_10.txt') as f:
	for line in f:
		grid.append([c for c in line.rstrip()])

w = len(grid[0])
h = len(grid)
covered = set()
path = []
start = None

for y in range(h):
	for x in range(w):
		coords = (x, y)

		if grid[y][x] == '.' or coords in covered:
			continue

		direction = (0, 0)
		path.clear()

		while True:
			if coords in covered:
				break

			if coords[0] < 0 or coords[0] >= w or coords[1] < 0 or coords[1] >= h:
				break

			covered.add(coords)
			path.append(coords)
			current = grid[coords[1]][coords[0]]

			match current:
				case 'S':
					start = coords
					up = grid[coords[1] - 1][coords[0]] in CONNECTS_DOWN if y > 0 else False
					down = grid[coords[1] + 1][coords[0]] in CONNECTS_UP if y < h - 1 else False
					left = grid[coords[1]][coords[0] - 1] in CONNECTS_RIGHT if x > 0 else False
					right = grid[coords[1]][coords[0] + 1] in CONNECTS_LEFT if x < w - 1 else False

					if up:
						if down:
							actual = '|'
						else:
							actual = 'J' if left else 'L'
					elif down:
						actual = '7' if left else 'F'
					else:
						actual = '-'

					direction = alter_direction(actual, direction, coords, w, h)

				case '.':
					break

				case _:
					direction = alter_direction(current, direction, coords, w, h)

					if direction == (0, 0):
						covered.remove(coords)

						break

			coords = (coords[0] + direction[0], coords[1] + direction[1])

		if start:
			break

	if start:
		break

furthest = len(path) / 2

print(furthest)
