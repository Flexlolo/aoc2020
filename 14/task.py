import re
import sys

# with open('test2') as f:
with open('input') as f:
	lines = f.read().splitlines()


def mask_apply_value(value: int, mask: str) -> int:
	if value:
		v = list(f'{value:036b}')

		for bit in range(36):
			if mask[bit] == 'X':
				continue
			else:
				v[bit] = mask[bit]
	else:
		v = mask.replace('X', '0')

	return int(''.join(v), 2)

def part1():
	mem = {}
	mask = ''

	for i, line in enumerate(lines):
		if (m := re.match(r'mask = (.+)', line)):
			mask = m.group(1)
		elif (m := re.match(r'mem\[(\d+)\] = (\d+)', line)):
			addr = int(m.group(1))
			value = int(m.group(2))

			mem[addr] = mask_apply_value(value, mask)


	s = 0

	for v in mem.values():
		s += v

	print(f'part 1: {s}')



def mask_apply_addr(addr: int, mask: str) -> str:
	if addr:
		v = list(f'{addr:036b}')

		for bit in range(36):
			if mask[bit] == '0':
				continue
			else:
				v[bit] = mask[bit]
	else:
		v = mask

	return ''.join(v)



from typing import List
from copy import deepcopy

def addr_permute(addr: List[str])-> List[List[str]]:
	for bit in range(len(addr)):
		if addr[bit] == 'X':
			r = addr_permute(addr[bit + 1:])
			p = [deepcopy(r), deepcopy(r)]

			for i in range(2):
				for l in p[i]:
					l.insert(0, str(i))

					if bit:
						for j in range(bit):
							l.insert(0, addr[bit - j - 1])

			return p[0] + p[1]

	return [addr]

def part2():

	# for p in addr_permute(['0', 'X', '0', 'X', '1']):
	# 	print(''p)


	mem = {}
	mask = ''

	for i, line in enumerate(lines):
		if (m := re.match(r'mask = (.+)', line)):
			mask = m.group(1)
		elif (m := re.match(r'mem\[(\d+)\] = (\d+)', line)):
			addr = int(m.group(1))
			value = int(m.group(2))

			addr_mask = list(mask_apply_addr(addr, mask))

			for p in addr_permute(addr_mask):
				addr = int(''.join(p), 2)
				mem[addr] = value

	s = 0

	for v in mem.values():
		s += v

	print(f'part 2: {s}')

part2()