class Node:
	def __init__(self, edges):
		self.edges = edges

def process(workflow):
	edges = []
	negated = []

	for letter, condition, comparison, send in workflow:
		acceptable = []

		if comparison:
			spread = (1, comparison - 1) if condition == '<' else (comparison + 1, 4000)
			acceptable.append((letter, spread))

		if send != 'R':
			acceptable.extend(negated)
			edges.append((acceptable, send))

		if comparison:
			opposite = (spread[1] + 1, 4000) if spread[0] == 1 else (1, spread[0] - 1)
			negated.append((letter, opposite))

	return Node(edges)

def recurse(nodes, key, results):
	if not key in nodes:
		return 0

	total = 0

	for acceptable, send in nodes[key].edges:
		if len(acceptable) > 0:
			restore = {}

			for local in 'xmas':
				restore[local] = results[local].copy()

			for local, spread in acceptable:
				array = results[local]
				array[0] = max(array[0], spread[0])
				array[1] = min(array[1], spread[1])

		if send == 'A':
			local = 1

			for local_letter in 'xmas':
				minimum, maximum = results[local_letter]
				local *= maximum - minimum + 1

			total += local
		else:
			total += recurse(nodes, send, results)

		if len(acceptable) > 0:
			for local in 'xmas':
				for i in range(2):
					results[local][i] = restore[local][i]

	return total

def traverse(nodes):
	results = {}

	for letter in 'xmas':
		results[letter] = [1, 4000]

	return recurse(nodes, 'in', results)

workflows = {}

with open('day_19.txt') as f:
	for line in f:
		stripped = line.rstrip()

		if len(stripped) == 0:
			break

		brace = stripped.index('{')
		workflow = stripped[:brace]
		tokens = stripped[(brace + 1):-1].split(',')
		rules = []

		for i, token in enumerate(tokens):
			if i == len(tokens) - 1:
				send = token
				parameters = (None, None, None, send)
			else:
				arrow = token.index('>') if '>' in token else token.index('<')
				colon = token.index(':')
				letter = token[:arrow]
				condition = token[arrow]
				comparison = int(token[(arrow + 1):colon])
				send = token[(colon + 1):]
				parameters = (letter, condition, comparison, send)
				
			rules.append(parameters)

		workflows[workflow] = rules

nodes = {}

for key, value in workflows.items():
	node = process(value)

	if len(node.edges) > 0:
		nodes[key] = node

print(traverse(nodes))
