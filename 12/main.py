import re
from operator import add

with open('input') as f:
	plan = [line for line in f.read().splitlines()]

dirs = {
	'E': (1, 0), 
	'S': (0, -1), 
	'W': (-1, 0), 
	'N': (0, 1)
}

# part 1

d = 'E'
p = (0, 0)

for line in plan:

	if (m := re.match(r'([ESWN])(\d+)', line)):
		step = tuple([i * int(m.group(2)) for i in dirs[m.group(1)]])
		p = tuple(map(sum, zip(p, step)))

	elif (m := re.match(r'F(\d+)', line)):
		step = tuple([i * int(m.group(1)) for i in dirs[d]])
		p = tuple(map(sum, zip(p, step)))

	elif (m := re.match(r'([LR])(\d+)', line)):
		rot_dir = -1 if m.group(1) == 'L' else 1
		rot = int(m.group(2)) // 90
		dir_keys = list(dirs.keys())
		d = dir_keys[(dir_keys.index(d) + rot_dir * rot) % len(dirs)]

print(abs(p[0]) + abs(p[1]))


# part 2

p = (0, 0)

waypoint = {
	'E': 10, 
	'S': 0,
	'W': 0,
	'N': 1
}

for line in plan:
	if (m := re.match(r'([ESWN])(\d+)', line)):
		waypoint[m.group(1)] += int(m.group(2))

	elif (m := re.match(r'F(\d+)', line)):
		step = (0, 0)

		for d in waypoint:
			mv = tuple(i * waypoint[d] for i in dirs[d])
			step = tuple(map(sum, zip(step, mv)))

		step = tuple([i * int(m.group(1)) for i in step])
		p = tuple(map(sum, zip(p, step)))

	elif (m := re.match(r'([LR])(\d+)', line)):
		rot_dir = -1 if m.group(1) == 'L' else 1
		rot = int(m.group(2)) // 90
		dir_keys = list(dirs.keys())

		waypoint_new = {}

		for d in waypoint:
			d_new = dir_keys[(dir_keys.index(d) + rot_dir * rot) % len(dirs)]
			waypoint_new[d_new] = waypoint[d]

		waypoint = waypoint_new

print(abs(p[0]) + abs(p[1]))
