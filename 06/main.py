# part 1
total = 0

with open('input') as f:
	for group in f.read().split('\n\n'):
		answers = set()

		for line in group.splitlines():
			for letter in line:
				answers.add(letter)

		total += len(answers)

print(total)

# part 2
total = 0

with open('input') as f:
	for group in f.read().split('\n\n'):
		for i, line in enumerate(group.splitlines()):
			s = set([l for l in line])
			if i:
				common = s.intersection(common)
			else:
				common = s

		total += len(common)

print(total)