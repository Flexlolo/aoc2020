import math
from typing import Tuple

data = []

with open('input') as f:
	data = f.read().splitlines()

	scale = math.ceil(len(data) / len(data[0])) * 10
	data = [line * scale for line in data]


def check(slope: Tuple[int, int]):
	count = 0
	pos = (1, 1)

	while True:
		try:
			pos = (pos[0] + slope[0], pos[1] + slope[1])
			if data[pos[0] - 1][pos[1] - 1] == '#':
				count += 1
		except IndexError:
			return count	

# part1
print(check((1, 3)))

# part2
total = 1

for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
	total *= check(slope)

print(total)