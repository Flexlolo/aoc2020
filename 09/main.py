with open('input') as f:
	numbers = [int(i) for i in f.read().splitlines()]


# part 1

def check_preamble(numbers, i):
	for i1, n1 in enumerate(numbers[i-25:i]):
		for i2, n2 in enumerate(numbers[i-25:i]):
			if i1 != i2:
				if n1 + n2 == numbers[i]:
					return True
	return False

for i, n in enumerate(numbers):
	if i < 25:
		continue

	if not check_preamble(numbers, i):
		print(f'{i} ({numbers[i]}) not valid!')
		break

# part 2

total = numbers[i]
numbers = [n for n in numbers if n < total]
l = len(numbers)

for i in range(l):
	j = 0

	while True:
		j += 1
		s = sum(numbers[l-i-j-1:l-i-1])

		if s > total:
			break
		elif s == total:
			h = max(numbers[l-i-j-1:l-i-1])
			l = min(numbers[l-i-j-1:l-i-1])

			print('found it!')
			print(h + l)

			import sys
			sys.exit(0)