code = []

with open('input') as f:
	for line in f.read().splitlines():
		op, num = line.split(' ')
		code.append((op, int(num)))

# part 1

i = 0
acc = 0
seen = set()
jmps = []
nops = []

while True:
	if i in seen:
		break

	seen.add(i)

	op, num = code[i]
	# print(op, num)

	if op == 'acc':
		acc += num
		i += 1
	elif op == 'jmp':
		jmps.append(i)
		i += num
	elif op == 'nop':
		nops.append(i)
		i += 1

print(acc)

# part 2

def repair(code, i):
	test = code.copy()

	if test[i][0] == 'jmp':
		test[i] = ('nop', test[i][1])
	else:
		test[i] = ('jmp', test[i][1])

	return test

def terminates(code):
	i = 0
	acc = 0
	seen = set()

	while True:
		if i == len(code):
			return True, acc

		if i in seen:
			return False, 0

		seen.add(i)
		op, num = code[i]

		if op == 'acc':
			acc += num
			i += 1
		elif op == 'jmp':
			i += num
		elif op == 'nop':
			i += 1

for i in jmps:
	if terminates(repair(code, i))[0]:
		print(f'ITS JMP #{i}')
		print(terminates(repair(code, i))[1])

for i in nops:
	if terminates(repair(code, i))[0]:
		print(f'ITS NOP #{i}')
		print(terminates(repair(code, i))[1])