from typing import List, Tuple
import re
import itertools
import time

class Rules:

	def __init__(self, rules: List[str]):
		self.rules = {}

		for line in rules:
			if (m := re.match(r'(\d+): "(\w+)"', line)):
				n = int(m.group(1))
				c = m.group(2)
				self.rules[n] = c
			elif (m := re.match(r'(\d+): ((\d+)( \d+)*)( \| ((\d+)( \d+)*))?', line)):
				n = int(m.group(1))

				subrules = []
				sr1 = m.group(2)
				sr2 = m.group(6)

				sr1 = tuple(int(i) for i in sr1.split(' '))

				if sr2:
					sr2 = tuple(int(i) for i in sr2.split(' '))

				self.rules[n] = (sr1, sr2)

	def is_valid(self, pattern: str, rule: int = 0) -> Tuple[bool, bool, List[str]]:
		if isinstance(self.rules[rule], str):
			lit = self.rules[rule]

			if pattern == lit:
				return (True, False, [pattern])
			elif pattern.startswith(lit):
				return (False, True, [lit])
			else:
				return (False, False, [])

		def check_rule_prefix(pattern: str, prefix: str, rule: int):
			pattern_new = pattern.replace(prefix, '', 1)
			equal, starts, candidates = self.is_valid(pattern_new, r)
			if starts:
				for candidate in candidates:
					yield prefix + candidate

		ret = (False, False, [])

		for sr in self.rules[rule]:
			if sr is None:
				continue
			
			if len(sr) == 1:
				equal, starts, candidates = self.is_valid(pattern, sr[0])

				if equal:
					return (True, False, candidates)
				elif starts:
					ret = (False, True, candidates)
			else:
				valid = True
				prefixes = ['']

				for r in sr[:-1]:
					prefixes_new = []

					for prefix in prefixes:
						res = [*check_rule_prefix(pattern, prefix, r)]
						prefixes_new += res

					prefixes = prefixes_new

				for prefix in prefixes:
					pattern_new = pattern.replace(prefix, '', 1)
					equal, starts, candidates = self.is_valid(pattern_new, sr[-1])

					if equal:
						return (True, False, candidates)
					elif starts:
						candidates_new = [prefix + c for c in candidates]
						ret = (False, True, [*ret[-1], *candidates_new])

		return ret

	def validate(self, pattern: str) -> bool:
		equal, starts, candidates = self.is_valid(pattern, 0)
		return equal


# with open('testinput') as f:
with open('input') as f:
	data = f.read()

rules, data = data.split('\n\n')
rules = rules.splitlines()
data = data.splitlines()

R = Rules(rules)

def count():
	matches = 0

	for pattern in data:
		if R.validate(pattern):
			matches += 1

	return matches

print('PART 1:', count())

R.rules[8] = ((42,), (42, 8))
R.rules[11] = ((42, 31), (42, 11, 31))
print('PART 2:', count())