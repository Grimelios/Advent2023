import sys

lowest = sys.maxsize

with open('day_05.txt') as f:
	lines = [line.rstrip() for line in f]
	i = 0
	seeds = [int(part) for part in lines[0][7:].split(' ')]
	range_lists = []
	i = 2

	while i < len(lines):
		parts = lines[i][:-5].split('-')
		s_from = parts[0]
		s_to = parts[1]
		i += 1
		ranges = []

		while i < len(lines) and len(lines[i]) > 0:
			parts = lines[i].split(' ')
			dest_start = int(parts[0])
			source_start = int(parts[1])
			range_length = int(parts[2])
			ranges.append((dest_start, source_start, range_length))
			i += 1

		range_lists.append(ranges)
		i += 1

	for seed in seeds:
		current = seed

		for range_list in range_lists:
			for dest_start, source_start, range_length in range_list:
				delta = current - source_start

				if delta >= 0 and delta < range_length:
					current = dest_start + delta

					break

		lowest = min(lowest, current)

print(lowest)
