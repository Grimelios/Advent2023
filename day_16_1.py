grid = []

with open('day_16.txt') as f:
	for line in f:
		grid.append(line.rstrip())

w = len(grid[0])
h = len(grid)
beams = [(-1, 0, 1, 0)]
path = set()
energized = set()
is_first_iteration = True

while len(beams) > 0:
	i = len(beams) - 1

	while i >= 0:
		beam = beams[i]
		vX = beam[2]
		vY = beam[3]
		pX = beam[0]
		pY = beam[1]
		key = (pX, pY, vX, vY)

		if key in path:
			del beams[i]

			i -= 1

			continue

		if not is_first_iteration:
			path.add(key)
			energized.add((pX, pY))

		is_first_iteration = False
		pX += vX
		pY += vY

		if pX < 0 or pX >= w or pY < 0 or pY >= h:
			del beams[i]

			i -= 1

			continue

		tile = grid[pY][pX]

		match tile:
			case '|':
				if vX != 0:
					vX = 0
					vY = -1
					beams.append((pX, pY, 0, 1))

			case '-':
				if vY != 0:
					vX = -1
					vY = 0
					beams.append((pX, pY, 1, 0))

			case '\\':
				if vX != 0:
					vY = vX
					vX = 0
				else:
					vX = vY
					vY = 0

			case '/':
				if vX != 0:
					vY = -vX
					vX = 0
				else:
					vX = -vY
					vY = 0

		beams[i] = (pX, pY, vX, vY)
		i -= 1

print(len(energized))
