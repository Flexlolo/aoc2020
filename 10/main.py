with open('input') as f:
	adapters = [int(i) for i in f.read().splitlines()] + [0] 

# part 1
adapters = sorted(adapters)

diffs = [3]

for i in range(len(adapters) - 1):
	d = adapters[i + 1] - adapters[i]
	diffs.append(d)


print(diffs.count(1) * diffs.count(3) )

# part 2

hmm = []

for i in range(1, len(adapters) - 1):
	d = adapters[i + 1] - adapters[i - 1]

	if d <= 3:
		hmm.append(adapters[i])

total = 1
i = 0

while True:
	l = len(hmm)

	if i >= l:
		break

	if i + 1 < l and hmm[i + 1] - hmm[i] == 1:
		if i + 2 < l and hmm[i + 2] - hmm[i + 1] == 1:
			total *= 7
			i += 3
		else:
			total *= 4
			i += 2
	else:
		total *= 2
		i += 1

print(total)