import re

rules = []

with open('input') as f:
	for line in f.read().splitlines():
		m = re.match('(.+) bags contain (.+)', line)
		color = m.group(1)

		for bag in m.group(2).split(','):
			if bag.find('no other bags') != -1:
				count, contain = 0, None
			else:
				count, contain = re.findall(r'(\d+) (.+) bag', bag)[0]

			rules.append((color, contain, int(count)))

# part 1
queue = ['shiny gold']
seen = set()

while True:
	if not queue:
		break

	new = []

	for item in queue:
		if item not in seen:
			for rule in rules:
				if rule[1] == item:
					new.append(rule[0])

			seen.add(item)

	queue = new

print(len(seen) - 1)

# part 2
queue = ['shiny gold']
seen = set()

def get_count(color):
	count = 0

	for rule in rules:
		if rule[0] == color:
			if rule[2]:
				count += rule[2] * (get_count(rule[1])  + 1)
	return count

print(get_count('shiny gold'))
