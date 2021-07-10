from copy import copy
from typing import List

from collections import defaultdict

def solve(input_data: List[int], length: int) -> int:
	stack = list()
	lookup = defaultdict(list)

	while len(stack) != length:
		size = len(stack)

		if size < len(input_data):
			last = input_data[size]
			lookup[last].append(size)
			stack.append(last)
		else:
			last = stack[-1]

			if last in lookup and len(lookup[last]) > 1:
				distance = lookup[last][-1] - lookup[last][-2]
			else:
				distance = 0

			lookup[distance].append(size)
			stack.append(distance)

		if size % 50000 == 0:
			print('step:', size)

		# print(f'{size = } | {dict(lookup) = }')

	# print(stack)
	return stack[-1]


data = [2,0,6,12,1,3]

data_test = [0,3,6]
# data = data_test

# print(solve(data, 10))

# part 1
print(solve(data, 2020))

# part 2
print(solve(data, 30000000))
