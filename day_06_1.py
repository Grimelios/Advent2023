with open('day_06.txt') as f:
	lines = [line.rstrip() for line in f]

times = [int(part.strip()) for part in lines[0].split(':')[1].split(' ') if len(part) > 0]
distances = [int(part.strip()) for part in lines[1].split(':')[1].split(' ') if len(part) > 0]
margin = 1

for i in range(len(times)):
	time = times[i]
	distance = distances[i]
	ways = 0

	for j in range(time):
		traveled = (time - j) * j;
		
		if traveled > distance:
			ways += 1

	margin *= ways

print(margin)
