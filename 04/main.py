import re

def is_valid_1(fields):
	KEYS = (
		'byr',
		'iyr',
		'eyr',
		'hgt',
		'hcl',
		'ecl',
		'pid',
		'cid',
	)

	fields = [i for i, _ in fields]

	for key in KEYS:
		if key != 'cid' and key not in fields:
			return False

	return True

def is_valid_2(fields):
	for key, value in fields:
		if key == 'byr':
			if 1920 <= int(value) <= 2002:
				continue

		elif key == 'iyr':
			if 2010 <= int(value) <= 2020:
				continue

		elif key == 'eyr':
			if 2020 <= int(value) <= 2030:
				continue

		elif key == 'hgt':
			if (m := re.match(r'(\d+)cm', value)):
				if 150 <= int(m.group(1)) <= 193:
					continue
			elif (m := re.match(r'(\d+)in', value)):
				if 59 <= int(m.group(1)) <= 76:
					continue

		elif key == 'hcl':
			if (m := re.match(r'#[0-9a-f]{6}', value)):
				continue

		elif key == 'ecl':
			if value in 'amb blu brn gry grn hzl oth'.split(' '):
				continue

		elif key == 'pid':
			if len(value) == 9:
				continue

		elif key == 'cid':
			continue

		return False

	return True


# part 1
valid = 0

with open('input') as f:
	for line in f.read().split('\n\n'):
		fields = re.findall(r'(\w+):(\S+)', line)

		if is_valid_1(fields):
			valid += 1

print(valid)
			
# part 2
valid = 0

with open('input') as f:
	for line in f.read().split('\n\n'):
		fields = re.findall(r'(\w+):(\S+)', line)

		if is_valid_1(fields) and is_valid_2(fields):
			valid += 1

print(valid)
