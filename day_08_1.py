with open('day_08.txt') as f:
	lines = [line.rstrip() for line in f]

directions = lines[0]
nodes = {}

for i in range(len(lines) - 2):
	line = lines[i + 2]
	delimiter = line.index('=')
	node = line[:(delimiter - 1)]
	parts = line[(delimiter + 3):-1].split(',')
	nodes[node] = (parts[0], parts[1][1:])

i = 0
steps = 0
current = 'AAA'

while current != 'ZZZ':
	turn = 0 if directions[i] == 'L' else 1
	i = (i + 1) % len(directions)
	current = nodes[current][turn]
	steps += 1

print(steps)
