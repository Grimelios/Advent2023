total = 0

with open('day_09.txt') as f:
	for line in f:
		values = [int(part) for part in line.rstrip().split(' ')]
		rows = []
		rows.append(values)

		while True:
			deltas = []

			for i in range(len(values) - 1):
				deltas.append(values[i + 1] - values[i])

			rows.append(deltas)

			if all([delta == 0 for delta in deltas]):
				break

			values = deltas

		extrapolated = 0

		for i in range(len(rows) - 1):
			last = rows[-(i + 2)][-1]
			extrapolated += last

		total += extrapolated

print(total)
