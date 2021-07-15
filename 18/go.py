with open('input') as f:
	data = f.read().splitlines()


from calculator import Calculator


def solve(task: str):
	# print(task)
	result = Calculator.calculate(task)
	# print(result)
	return result

# part 1
s = 0

for task in data:
	s += solve(task)

# change precedence in calculator depending on part
print('ANSWER', s)
