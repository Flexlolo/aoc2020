from copy import deepcopy

def show(seats):
	for line in seats:
		print(''.join(line))

def getadj(seats, x, y, infinite=False):
	count = 0

	for dx, dy in [	(0, 1), (1, 0), (1, 1), 
					(0, -1), (-1, 0), (-1, -1),
					(1, -1), (-1, 1)]:

		if infinite:
			i = 0

			while True:
				i += 1
				nx = x + dx * i
				ny = y + dy * i

				if nx < 0 or ny < 0:
					break

				try:
					tile = seats[ny][nx]

					if tile == '.':
						continue
					else:
						if seats[ny][nx] == '#':
							count += 1

						break

				except Exception:
					break

		else:
			nx = x + dx
			ny = y + dy

			if nx < 0 or ny < 0:
				continue

			try:
				if seats[ny][nx] == '#':
					count += 1
			except Exception:
				pass

	return count

def step(seats, infinite=False):
	new = deepcopy(seats)

	for y in range(len(seats)):
		for x in range(len(seats[0])):
			tile = seats[y][x]

			if tile == '.':
				continue

			count = getadj(seats, x, y, infinite)
			mincount = 4

			if infinite:
				mincount = 5

			if tile == '#' and count >= mincount:
				new[y][x] = 'L'
			elif tile == 'L' and count == 0:
				new[y][x] = '#'

	return new

# part 1
with open('input') as f:
	seats = [[i for i in line] for line in f.read().splitlines()]

while True:
	new = step(seats)

	if new == seats:
		print(sum([line.count('#') for line in seats]))
		break

	seats = new

# part 2
with open('input') as f:
	seats = [[i for i in line] for line in f.read().splitlines()]

while True:
	# print('------------------')
	# show(seats)
	# print('------------------')

	new = step(seats, True)

	if new == seats:
		print(sum([line.count('#') for line in seats]))
		break

	seats = new