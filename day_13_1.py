def analyze(pattern):
	w = len(pattern[0])
	h = len(pattern)

	for split in range(w - 1):
		limit = min(split + 1, w - split - 1)
		split_confirmed = True

		for x in range(limit):
			for y in range(h):
				if pattern[y][split + 1 + x] != pattern[y][split + 1 - (x + 1)]:
					split_confirmed = False

					break

			if not split_confirmed:
				break

		if split_confirmed:
			break

	if split_confirmed:
		return split + 1

	for split in range(h - 1):
		limit = min(split + 1, h - split - 1)
		split_confirmed = True

		for y in range(limit):
			for x in range(w):
				if pattern[split + 1 + y] != pattern[split + 1 - (y + 1)]:
					split_confirmed = False

					break


			if not split_confirmed:
				break

		if split_confirmed:
			break

	return (split + 1) * 100

with open('day_13.txt') as f:
	rows = [line.rstrip() for line in f]

pattern = []
i = 0
total = 0

while i < len(rows):
	row = rows[i]
	i += 1

	if len(row) > 0:
		pattern.append(row)

		continue

	total += analyze(pattern)
	pattern.clear()

total += analyze(pattern)

print(total)
