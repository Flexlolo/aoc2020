def decode(string):

	chars = {
		'F': '0',
		'B': '1',
		'R': '1',
		'L': '0'
	}
	row = int(''.join([chars[c] for c in string[:7]]), 2)
	col = int(''.join([chars[c] for c in string[7:]]), 2)

	return row * 8 + col

# part1 
highest = 0

seats = set()

with open('input') as f:
	for line in f.read().splitlines():
		seat = decode(line)

		if seat > highest:
			highest = seat

		seats.add(seat)

print(highest)

# part 2
for i in range(0, highest):
	if i not in seats:
		print(f'{i} is missing!')