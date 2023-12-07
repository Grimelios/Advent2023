sum = 0

spelled = [
	'zero',
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine'
]

with open('day_01.txt') as f:
	for line in f:
		first = None
		last = None

		for i, c in enumerate(line):
			if c.isdigit():
				first = c
			else:
				for j, s in enumerate(spelled):
					if line[i:][:len(s)] == s:
						first = str(j)

						break

			if first:
				break

		for i in reversed(range(len(line))):
			c = line[i]

			if c.isdigit():
				last = c
			else:
				for j, s in enumerate(spelled):
					if line[i:][:len(s)] == s:
						last = str(j)

						break

			if last:
				break

		sum += int(first + last)

print(sum)
