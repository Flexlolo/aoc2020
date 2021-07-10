from typing import Tuple

from collections import defaultdict
import itertools
from copy import deepcopy

Coords = Tuple

#
# SIMULATION
#

def get_state(grid, c: Coords):
	global DIMENSIONS

	if DIMENSIONS == 3:
		x,y,z = c
		return grid[z][y][x]
	else:
		x,y,z,w = c
		return grid[w][z][y][x]


def set_state(grid, c: Coords, value):
	global DIMENSIONS

	if DIMENSIONS == 3:
		x,y,z = c
		grid[z][y][x] = value
	else:
		x,y,z,w = c
		grid[w][z][y][x] = value


def coordinates_get(grid, hyper: bool = True):
	global DIMENSIONS

	if hyper and DIMENSIONS == 4:
		for w, wg in grid.items():
			for x,y,z in coordinates_get(wg, False):
				yield (x,y,z,w)
	else:
		for z, zg in grid.items():
			for y, yg in zg.items():
				for x, v in yg.items():
					yield (x, y, z)

def neighbours_get(grid, c: Coords):
	ranges = [[v - 1, v, v + 1] for v in c]

	for product in itertools.product(*ranges):
		if product != c:
			yield product

def count_active(grid):
	count = 0

	for c in coordinates_get(grid):
		if get_state(grid, c):
			count += 1

	return count

def debug(grid):
	global DIMENSIONS

	if DIMENSIONS != 3:
		print('Debug not supported.')
		return

	for z, zg in sorted(grid.items()):
		lines = []

		for y, yg in sorted(zg.items()):
			line = []

			for x, v in sorted(yg.items()):
				line.append('#' if v else '.')
				# print(f'{x=},{y=},{z=} | {v=}')

			lines.append(''.join(line))

		print(f'{z=}')
		print('\n'.join(lines))
		print('\n')

def simulate_point(grid, grid_new, seen, c: Coords, neighbours):
	if c in seen:
		return

	state = get_state(grid, c)
	neighbours_state = [get_state(grid, n) for n in neighbours]
	active_count = neighbours_state.count(True)

	state_new = False
	
	if state:
		if active_count in (2,3):
			state_new = True

	else:
		if active_count == 3:
			state_new = True

	set_state(grid_new, c, state_new)
	seen.add(c)

def simulation(grid):
	grid_new = deepcopy(grid)
	seen = set()
	coordinates = [c for c in coordinates_get(grid)]

	for c in coordinates:
		neighbours = [n for n in neighbours_get(grid, c)]
		simulate_point(grid, grid_new, seen, c, neighbours)

	for c in coordinates:
		for nc in neighbours_get(grid, c):
			neighbours = [n for n in neighbours_get(grid, nc)]
			simulate_point(grid, grid_new, seen, nc, neighbours)

	return grid_new
	

#
# SOLUTION
#

def solve(dimensions: int):
	global DIMENSIONS
	DIMENSIONS = dimensions

	if DIMENSIONS == 3:
		grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
	else:
		grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False))))

	# READ DATA
	with open('input') as f:
		w = 0
		z = 0

		for y, line in enumerate(f.read().splitlines()):
			for x, ch in enumerate(line):
				state = True if ch == '#' else False

				if DIMENSIONS == 3:
					c = (x, y, z)
				else:
					c = (x, y, z, w)

				set_state(grid, c, state)


	# RUN SIMULATION
	for step in range(6):
		print('STEP:', step + 1)
		# debug(grid)
		grid = simulation(grid)

	# debug(grid)
	return count_active(grid)



print('PART 1:', solve(3))
print('PART 2:', solve(4))
