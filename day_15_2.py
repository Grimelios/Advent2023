def analyze(s):
	label = ''
	index = 0
	i = 0

	while i < len(s):
		c = s[i]
		i += 1

		if c in ['-', '=']:
			break

		label += c
		index += ord(c)
		index *= 17
		index = index % 256

	operation = c
	focal_length = int(s[i]) if operation == '=' else 0
	
	return label, index, operation, focal_length

with open('day_15.txt') as f:
	parts = next(line.rstrip() for line in f).split(',')

boxes = []

for i in range(256):
	boxes.append([])

for part in parts:
	label, index, operation, focal_length = analyze(part)
	box = boxes[index]

	if operation == '-':
		for i in range(len(box)):
			if box[i][0] == label:
				del box[i]
				break
	else:
		replaced = False

		for i in range(len(box)):
			labeled, f = box[i]

			if labeled == label:
				box[i] = (label, focal_length)
				replaced = True

				break

		if not replaced:
			box.append((label, focal_length))

power = 0

for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		power += (i + 1) * (j + 1) * lens[1]

print(power)
