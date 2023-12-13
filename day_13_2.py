def analyze(pattern, comparison):
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
			if (1, split) != comparison:
				break

			split_confirmed = False

	if split_confirmed:
		return (1, split)

	for split in range(h - 1):
		limit = min(split + 1, h - split - 1)
		split_confirmed = True

		for y in range(limit):
			for x in range(w):
				if pattern[split + 1 + y][x] != pattern[split + 1 - (y + 1)][x]:
					split_confirmed = False

					break


			if not split_confirmed:
				break

		if split_confirmed:
			if (100, split) != comparison:
				break

			split_confirmed = False

	if split_confirmed:
		return (100, split)

	return (0, -1)

def analyze_with_smudge(pattern):
	original = analyze(pattern, None)
	w = len(pattern[0])
	h = len(pattern)

	for y in range(h):
		for x in range(w):
			current = pattern[y][x]
			pattern[y][x] = '.' if current == '#' else '#'
			result = analyze(pattern, original)

			if result[1] >= 0:
				return result[0] * (result[1] + 1)

			pattern[y][x] = current

	return 0

with open('day_13.txt') as f:
	rows = [line.rstrip() for line in f]

pattern = []
i = 0
total = 0

while i < len(rows):
	row = rows[i]
	i += 1

	if len(row) > 0:
		pattern.append([c for c in row])

		continue

	total += analyze_with_smudge(pattern)
	pattern.clear()

total += analyze_with_smudge(pattern)

print(total)
