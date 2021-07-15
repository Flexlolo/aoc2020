from typing import List, Tuple, Union, Optional
import re
import time

class Calculator:

	OP = (
		# {
		# 	'**': lambda x, y: x ** y,
		# },
		# {
		# 	'*': lambda x, y: x * y,
		# 	'/': lambda x, y: x / y,
		# },
		# {
		# 	'+': lambda x, y: x + y,
		# 	'-': lambda x, y: x - y,
		# },

		# AOC
		{
			'+': lambda x, y: x + y,
			'-': lambda x, y: x - y,
		},

		{
			'*': lambda x, y: x * y,
		},
	)

	def parse_number(expr: str) -> Union[int, float]:
		if expr.find('.') != -1:
			return float(expr)

		return int(expr)

	def parse(expr: str) -> int:

		def parse_part(part: str):
			while part:
				stripped = part.strip()

				if stripped != part:
					part = stripped
					continue

				for bracket in '()':
					if part == bracket:
						parts.append(part)
						return

					elif bracket in part:
						before, after = part.split(bracket, 1)
						parse_part(before)
						parse_part(bracket)
						parse_part(after)
						return

				parts.append(part)
				return

		split = re.split(r'([\d]+(\.\d+)?)', expr)
		parts = []

		for part, value, _ in zip(*(iter(split),) * 3):
			parse_part(part)
			parts.append(Calculator.parse_number(value))

		if len(split) % 3 != 0:
			parse_part(split[-1])

		return parts
		
	def eval(expr: List[str]) -> Optional[Union[int, float]]:
		
		# simplify subexpr
		while True:
			if '(' in expr:
				start = expr.index('(')

				depth = 0
				i = start + 1

				while True:
					if expr[i] == '(':
						depth += 1
					if expr[i] == ')':
						if depth == 0:
							end = i
							break
						else:
							depth -= 1

					i += 1

				subexpr = expr[start + 1:end]
				result = Calculator.eval(subexpr)

				if result is not None:
					expr = expr[:start] + [result] + expr[end + 1:]
				else:
					expr = expr[:start] + expr[end + 1:]

				continue

			break

		# process expr
		if len(expr) > 1:
			ops = [g for g in Calculator.OP]

			while ops:
				group = ops.pop(0)
				keys = group.keys()

				i = 0
				while True:
					if i >= len(expr):
						break

					e = expr[i]

					if e in keys:
						result = group[e](expr[i-1], expr[i+1])
						expr = expr[:i-1] + [result] + expr[i+2:]
						i = 0
						continue

					i += 1

		if len(expr) == 1:
			return expr[0]

		return None


	def calculate(expr: str) -> Union[float, int]:
		parsed = Calculator.parse(expr)
		print(parsed)
		return Calculator.eval(parsed)