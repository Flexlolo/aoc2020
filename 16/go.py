import re
from typing import List, Dict, Tuple

#
# PROCESS DATA
#

with open('input') as f:
	data = f.read()


rules = {m.group(1).strip(): m.group(2) for m in re.finditer(r'([\w\s]+): (.+)', data) if m}

for key, rule in rules.items():
	rules[key] = [tuple(int(p) for p in r.split('-')) for r in rule.split(' or ')]


data = data.splitlines()


my_ticket = tuple(int(d) for d in data[data.index('your ticket:') + 1].split(','))

tickets = []

for line in data[data.index('nearby tickets:') + 1:]:
	ticket = tuple(int(d) for d in line.split(','))
	tickets.append(ticket)

# print(rules)
# print(my_ticket)
# print(tickets)

#
# SOLUTION
#

# PART 1
def part1(tickets: List[Tuple], rules: Dict[str, List[Tuple]]):

	def is_valid(value: int) -> bool:
		for rule in rules.values():
			for r in rule:
				if value >= r[0] and value <= r[1]:
					return True

		return False

	error_rate = 0
	invalid_tickets = set()

	for i, ticket in enumerate(tickets):
		for value in ticket:
			if not is_valid(value):
				error_rate += value

				if i not in invalid_tickets:
					invalid_tickets.add(i)

	print('PART 1:', error_rate)
	return invalid_tickets


invalid_tickets = part1(tickets, rules)

# PART 2
def part2(rules, my_ticket, tickets, invalid_tickets):
	delete_count = 0

	for index in sorted(invalid_tickets):
		del tickets[index - delete_count]
		delete_count += 1


	# check if value fits the rule
	def is_valid_rule(value: int, rule: List[Tuple]) -> bool:
		for r in rule:
			if value >= r[0] and value <= r[1]:
				return True

		return False

	# map possible fields to a row
	mapping = {}

	for i in range(len(tickets[0])):

		intersection = set()

		for n, ticket in enumerate(tickets):
			value = ticket[i]
			rules_work = set()

			for field, rule in rules.items():
				if is_valid_rule(value, rule):
					rules_work.add(field)

			if n == 0:
				intersection = rules_work
			else:
				intersection = intersection.intersection(rules_work)

			if len(intersection) == 1:
				break

		# if len(intersection) != 1:
			# print(intersection)
			# print('FUCK!')

		mapping[i] = intersection

	# solve mapping
	solution = {}

	while True:
		done = True

		for row, fields in mapping.items():
			if not fields:
				continue

			if len(fields):
				done = False

			if len(fields) == 1:
				field = list(fields)[0]
				solution[row] = field

				for other_fields in mapping.values():
					other_fields.discard(field)

		if done:
			break

	# print(solution)
	solved = {field: my_ticket[row] for row, field in solution.items()}
	# print(solved)

	result = 1

	for field in solved:
		if 'departure' in field:
			result *= solved[field]

	print('PART 2:', result)
	# for row in mapping:
	# 	print(mapping[row])
# print(mapping)

part2(rules, my_ticket, tickets, invalid_tickets)
