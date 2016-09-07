total = 0 
for character in table:
	total += table[character]
print total

for character in table:
	percentNumber = table[character] *100.0/total
	print "%s accounts for %f percent."%(character, percentNumber)