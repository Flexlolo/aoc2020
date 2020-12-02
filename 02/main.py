# part 1
valid = 0
with open('input') as f:
	for line in f.read().splitlines():
		count, letter, password = line.split(' ')
		count = [int(i) for i in count.split('-')]
		letter = letter[:-1]

		if count[0] <= password.count(letter) <= count[1]:
			valid += 1
print(valid)

# part 2
valid = 0
with open('input') as f:
	for line in f.read().splitlines():
		count, letter, password = line.split(' ')
		count = [int(i) for i in count.split('-')]
		letter = letter[:-1]

		valid_count = 0
		for pos in count:
			if password[pos - 1] == letter:
				valid_count += 1

		if valid_count == 1:
			valid += 1

print(valid)