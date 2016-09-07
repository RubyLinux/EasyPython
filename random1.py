table = {}
for character in "abcdefghijklmnopqrstuvwxyz":
	table[character] = 0
print table

myFile = open("/Users/Alex/Desktop/victorhugo.txt")
for line in myFile:
	for letter in line:
		letter = letter.lower()
		if letter in table:
			table[letter] += 1
print table