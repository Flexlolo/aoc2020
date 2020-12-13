# part 1
with open('input') as f:
	timestamp, buses = f.read().splitlines()
	timestamp = int(timestamp)
	buses = [int(i) for i in buses.split(',') if i != 'x']

import math

closest = 0
closest_bus = 0

for bus in buses:
	arrives = math.ceil(timestamp / bus) * bus
	wait = arrives - timestamp

	if not closest or closest > wait:
		closest = wait
		closest_bus = bus

print(closest * closest_bus)

# part 2
schedule = []
with open('input') as f:
	_, buses = f.read().splitlines()

	for i, bus in enumerate(buses.split(',')):
		if bus != 'x':
			schedule.append((i, int(bus)))

def solve(offset, lcm, n, o):
	print(f'solving for {offset} + {lcm} * n + {o}  %  {n}')
	
	i = 0
	while True:
		i += 1

		if (offset + lcm * i + o) % n == 0:
			return offset + lcm * i

lcm = schedule[0][1]
offset = 0
i = 0

while True:
	i += 1

	if i >= len(schedule):
		break

	o = schedule[i][0]
	n = schedule[i][1]
	offset = solve(offset, lcm, n, o)
	lcm *= n

print(offset)
