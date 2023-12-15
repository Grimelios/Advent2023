def hash_algorithm(s):
	current = 0

	for c in s:
		current += ord(c)
		current *= 17
		current = current % 256
	
	return current

with open('day_15.txt') as f:
	parts = next(line.rstrip() for line in f).split(',')

total = 0

for part in parts:
	total += hash_algorithm(part)

print(total)
