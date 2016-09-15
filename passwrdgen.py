import random

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pw_length = 8
mypassword = ""

for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypassword = mypassword + alphabet[next_index]

print(mypassword)
