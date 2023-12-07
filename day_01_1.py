sum = 0

with open('day_01.txt') as f:
	for line in f:
		for c in line:
			if c.isdigit():
				first = c

				break

		for c in reversed(line):
			if c.isdigit():
				last = c

				break

		sum += int(first + last)

print(sum)
