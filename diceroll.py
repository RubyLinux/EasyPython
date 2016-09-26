import random
min = 1
max = 6

roll = "yes"

while roll == "yes":
    print "The numbers on the dice are:"
    print random.randint(min, max)
    print random.randint(min, max)