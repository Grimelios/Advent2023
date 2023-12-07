with open('day_06.txt') as f:
	lines = [line.rstrip() for line in f]

time = int(''.join([part.strip() for part in lines[0].split(':')[1].split(' ') if len(part) > 0]))
distance = int(''.join([part.strip() for part in lines[1].split(':')[1].split(' ') if len(part) > 0]))
ways = 0

for i in range(time):
	traveled = (time - i) * i;
	
	if traveled > distance:
		ways += 1

print(ways)
