multiples = {3:0, 4:0, 5:0}

for i in range(1, 1001):
	if i % 3 == 0:
		multiples[3] += 1
	if i % 4 == 0:
		multiples[4] += 1
	if i % 5 == 0:
		multiples[5] += 1
print multiples