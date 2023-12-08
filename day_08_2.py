from math import lcm

def arrow_aligment(a, b, b_advantage):
	period, phase = combine_phased_rotations(a, 0, b, -b_advantage % b)

	return -phase % period

def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
	gcd, s, t = extended_gcd(a_period, b_period)
	phase_difference = a_phase - b_phase
	pd_mult, pd_remainder = divmod(phase_difference, gcd)
	combined_period = a_period // gcd * b_period
	combined_phase = (a_phase - s * pd_mult * a_period) % combined_period

	return combined_period, combined_phase

def extended_gcd(a, b):	
	old_r, r = a, b
	old_s, s = 1, 0
	old_t, t = 0, 1

	while r:
		quotient, remainder = divmod(old_r, r)
		old_r, r = r, remainder
		old_s, s = s, old_s - quotient * s
		old_t, t = t, old_t - quotient * t

	return old_r, old_s, old_t

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

	return combined_period, combined_phase

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

loop_b = loops.pop()

while len(loops) > 0:
	(offset_b, phase_b, z_b) = loop_b
	(offset_a, phase_a, z_a) = loops.pop()
	advantage = (offset_b + z_b[0]) - (offset_a + z_a[0])
	meet = arrow_aligment(phase_a, phase_b, advantage)
	z = meet + min(offset_a, offset_b)
	loop_b = (z, lcm(phase_a, phase_b), [0])

print(z)
