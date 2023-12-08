def find_loop(directions, nodes, node):
	z_list = []
	i = 0
	steps = 0
	current = node
	path = {}
	path[(current, 0)] = 0

	if current[-1] == 'Z':
		z_list.append(0)

	while True:
		turn = 0 if directions[i] == 'L' else 1
		i = (i + 1) % len(directions)
		steps += 1
		current = nodes[current][turn]

		if current[-1] == 'Z':
			z_list.append(steps)

		pair = (current, i)

		if pair in path:
			offset = path[pair]
			length = steps - offset
			z_index = 0

			while z_index < len(z_list) and z_list[z_index] < offset:
				z_index += 1

			return (offset, length, [z - offset for z in z_list[z_index:]])

		path[pair] = steps

with open('day_08.txt') as f:
	lines = [line.rstrip() for line in f]

directions = lines[0]
nodes = {}
starting = []

for i in range(len(lines) - 2):
	line = lines[i + 2]
	delimiter = line.index('=')
	node = line[:(delimiter - 1)]
	parts = line[(delimiter + 3):-1].split(',')
	nodes[node] = (parts[0], parts[1][1:])

	if node[-1] == 'A':
		starting.append(node)

loops = []

for n in starting:
	loops.append(find_loop(directions, nodes, n))

print('LOOPS %s' % loops)

loop_a = loops.pop()

while len(loops) > 0:
	loop_b = loops.pop() 
	index_a = loop_a[0] + loop_a[2][0]
	index_b = loop_b[0] + loop_b[2][0]

	print('A %s -> %s' % (index_a, loop_a[1]))
	print('B %s -> %s' % (index_b, loop_b[1]))

	while index_a != index_b:
		index_a += loop_a[1]
		index_b += loop_b[1]

	print('MEET %s' % index_a)

	quit()
