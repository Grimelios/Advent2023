import sys

def recurse(seeds, entries, entry_input, index, chain):
	if index == -1:
		entry_start = entry_input[0]
		entry_end = entry_start + entry_input[1] - 1

		for seed_pair in seeds:
			seed_start = seed_pair[0]
			seed_end = seed_start + seed_pair[1] - 1

			if seed_end < entry_start:
				continue

			if seed_start > entry_end:
				return sys.maxsize

			lowest_seed_within_range = max(seed_start, entry_start)
			current = lowest_seed_within_range

			for link in reversed(chain):
				current = link[2] + current - link[0]

			return current

		return sys.maxsize

	input_start = entry_input[0]
	input_range = entry_input[1]
	input_end = input_start + input_range - 1
	lowest = sys.maxsize

	for entry_current in entries[index]:
		output_value = entry_current[2]
		output_min = output_value
		output_max = output_value + entry_current[1] - 1
		output_range = output_max - output_min + 1

		if output_min > input_end or output_max < input_start:
			continue

		overlap_start = max(output_min, input_start)
		overlap_end = min(output_max, input_end)
		overlap_range = overlap_end - overlap_start + 1
		required_start = overlap_start - output_value + entry_current[0] 
		required_tuple = (required_start, overlap_range, output_value)
		chain.append(entry_current)
		lowest = min(lowest, recurse(seeds, entries, required_tuple, index - 1, chain))
		chain.pop()

	return lowest

with open('day_05.txt') as f:
	lines = [line.rstrip() for line in f]

numbers = [int(part) for part in lines[0].split(':')[1].split(' ') if len(part) > 0]
seeds = []
i = 0

while i < len(numbers):
	seed_start = int(numbers[i])
	seed_range = int(numbers[i + 1])
	seeds.append((seed_start, seed_range))
	i += 2

seeds.sort(key = lambda x: x[0])
entries = []
i = 2

while i < len(lines):
	i += 1
	raw = []

	while i < len(lines) and len(lines[i]) > 0:
		parts = lines[i].split(' ')
		dest_start = int(parts[0])
		source_start = int(parts[1])
		range_length = int(parts[2])
		raw.append((dest_start, source_start, range_length))
		i += 1

	raw.sort(key = lambda x: x[1])
	j = 0
	i += 1
	transformed = []
	last_end = -1

	while j < len(raw):
		entry = raw[j]
		start = entry[1]

		if start == last_end + 1:
			end = start + entry[2] - 1
			output = entry[0]
			j += 1
		else:
			end = start - 1
			start = last_end + 1
			output = start

		transformed.append((start, end - start + 1, output))
		last_end = end

	transformed.append((last_end + 1, sys.maxsize - (last_end + 1), last_end + 1))
	entries.append(transformed)

locations = entries[-1].copy()
locations.sort(key = lambda x: x[2])
lowest = sys.maxsize

for entry_input in locations:
	result = recurse(seeds, entries, entry_input, len(entries) - 2, [entry_input])
	lowest = min(lowest, result)

print(lowest)
