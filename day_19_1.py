def process(ratings, workflows):
	workflow = workflows['in']
	workflow_index = 0

	while workflow_index < len(workflow):
		(component, condition, comparison, send) = workflow[workflow_index]

		if component is None:
			if send == 'A':
				return True

			if send == 'R':
				return False

			workflow = workflows[send]
			workflow_index = 0

			continue

		value = ratings[component]
		passed = value > comparison if condition == '>' else value < comparison

		if passed:
			if send == 'A':
				return True

			if send == 'R':
				return False

			workflow = workflows[send]
			workflow_index = 0
		else:
			workflow_index += 1

workflows = {}
parts = []

with open('day_19.txt') as f:
	processing_workflows = True

	for line in f:
		stripped = line.rstrip()

		if len(stripped) == 0:
			processing_workflows = False

			continue

		if processing_workflows:
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
					component = token[:arrow]
					condition = token[arrow]
					comparison = int(token[(arrow + 1):colon])
					send = token[(colon + 1):]
					parameters = (component, condition, comparison, send)
					
				rules.append(parameters)

			workflows[workflow] = rules
		else:
			tokens = stripped[1:-1].split(',')
			ratings = {}
			total_rating = 0

			for token in tokens:
				equals = token.index('=')
				component = token[:equals]
				rating = int(token[(equals + 1):])
				ratings[component] = rating
				total_rating += rating

			parts.append((ratings, total_rating))

total = 0

for ratings, total_rating in parts:
	if process(ratings, workflows):
		total += total_rating

print(total)
