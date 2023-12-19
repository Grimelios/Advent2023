from functools import cmp_to_key

def sort_both(segment_a, segment_b):
	x_a = segment_a[0 if len(segment_a) == 5 else 2] 
	x_b = segment_b[0 if len(segment_b) == 5 else 2]

	if x_a < x_b:
		return -1

	return 1 if x_a > x_b else 0 

def sort_h(h_segment_a, h_segment_b):
	y_a = h_segment_a[4]
	y_b = h_segment_b[4]

	if y_a < y_b:
		return -1

	if y_a > y_b:
		return 1

	x_a = h_segment_a[0]
	x_b = h_segment_b[0]

	if x_a < x_b:
		return -1

	return 1 if x_a > x_b else 0

def sort_v(v_segment_a, v_segment_b):
	x_a = v_segment_a[2]
	x_b = v_segment_b[2]

	if x_a < x_b:
		return -1

	if x_a > x_b:
		return 1

	y_a = v_segment_a[0]
	y_b = v_segment_b[0]

	if y_a < y_b:
		return -1

	return 1 if y_a > y_b else 0

DIRECTION = ['R', 'D', 'L', 'U']

with open('day_18.txt') as f:
	lines = [line.rstrip() for line in f]

h_segments = []
v_segments = []
minimum = [0, 0]
maximum = [0, 0]
dug = 0
coords = [0, 0]
index = 0
directions = []

for i, line in enumerate(lines):
	hex_full = line.rstrip().split(' ')[2]
	direction = DIRECTION[int(hex_full[-2])]
	length = int(hex_full[2:-2], 16)
	dug += length
	v = [0, 0]

	match direction:
		case 'D':
			v[1] = 1

		case 'L':
			v[0] = -1

		case 'R':
			v[0] = 1

		case 'U':
			v[1] = -1

	previous = coords.copy()
	previous_direction = directions[-1] if i > 0 else ''
	directions.append(direction)
	coords[0] += v[0] * length
	coords[1] += v[1] * length
	minimum[0] = min(minimum[0], coords[0])
	minimum[1] = min(minimum[1], coords[1])
	maximum[0] = max(maximum[0], coords[0])
	maximum[1] = max(maximum[1], coords[1])

	if v[0] != 0:
		match direction:
			case 'L':
				corner = '7' if previous_direction == 'U' else 'J'
				corner_index = 3

			case 'R':
				corner = 'F' if previous_direction == 'U' else 'L'
				corner_index = 2

		xFrom = previous[0]
		xTo = coords[0]
		y = coords[1]

		if xFrom > xTo:
			xFrom, xTo = xTo, xFrom

		segment = [xFrom, xTo, '', '', y]
		segment[corner_index] = corner
		h_segments.append(segment)
	else:
		match direction:
			case 'D':
				corner = 'F' if previous_direction == 'L' else '7'

			case 'U':
				corner = 'L' if previous_direction == 'L' else 'J'

		last_h_segment = h_segments[-1]

		for i in range(2):
			if len(last_h_segment[i + 2]) == 0:
				last_h_segment[i + 2] = corner

				break

		yFrom = previous[1]
		yTo = coords[1]
		x = coords[0]

		if yFrom > yTo:
			yFrom, yTo = yTo, yFrom

		v_segments.append([yFrom, yTo, x])

h_first = h_segments[0]

if directions[-1] == 'U':
	if directions[0] == 'R':
		h_first[2] = 'F'
	else:
		h_first[3] = '7'
else:
	if directions[0] == 'R':
		h_first[2] = 'L'
	else:
		h_first[3] = 'J'

w = (maximum[0] - minimum[0]) + 1
h = (maximum[1] - minimum[1]) + 1
grid = []

for e in h_segments:
	e[0] -= minimum[0]
	e[1] -= minimum[0]
	e[4] -= minimum[1]

for e in v_segments:
	e[0] -= minimum[1]
	e[1] -= minimum[1]
	e[2] -= minimum[0]

for segment in v_segments:
	segment[0] += 1
	segment[1] -= 1

h_segments.sort(key = cmp_to_key(sort_h))
v_segments.sort(key = cmp_to_key(sort_v))

print_segments = False

if print_segments:
	print('HORIZONTAL')

	for e in h_segments:
		print(f'  {e}')

	print()
	print('VERTICAL')

	for e in v_segments:
		print(f'  {e}')

h_index = 0
v_index = 0

for y in range(h):
	relevant_h = []
	relevant_v = []
	original = dug

	while h_index < len(h_segments) and y == h_segments[h_index][4]:
		relevant_h.append(h_segments[h_index])
		h_index += 1

	for segment in v_segments:
		if y >= segment[0] and y <= segment[1]:
			relevant_v.append(segment)

	if len(relevant_v) == 0:
		if len(relevant_h) == 1:
			continue

		is_within = False

		for i, segment in enumerate(relevant_h):
			opener = segment[2]
			closer = segment[3]
			flip = (opener == 'F' and closer == 'J') or (opener == 'L' and closer == '7')

			if flip:
				is_within = not is_within

			if is_within and i < len(relevant_h) - 1:
				dug += relevant_h[i + 1][0] - segment[1] - 1
	elif len(relevant_h) == 0:
		for i in range(len(relevant_v) // 2):
			v_a = relevant_v[i * 2]
			v_b = relevant_v[i * 2 + 1]
			dug += v_b[2] - v_a[2] - 1
	else:
		combined = []
		combined.extend(relevant_h)
		combined.extend(relevant_v)
		combined.sort(key = cmp_to_key(sort_both))
		is_within = False

		for segment in combined:
			if is_within:
				to = segment[0 if len(segment) == 5 else 2]
				dug += to - x

			if len(segment) == 3:
				is_within = not is_within
				x = segment[2] + 1
			else:
				opener = segment[2]
				closer = segment[3]
				flip = (opener == 'F' and closer == 'J') or (opener == 'L' and closer == '7')
				x = segment[1] + 1

				if flip:
					is_within = not is_within

print(dug)
