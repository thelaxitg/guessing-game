import random

print("i am thinking of a number between 1 and 10 guess it in 5 tries ;)")
secret = random.randint(1, 10)
guess = 0
attempts = 0
limit = 5
out_of_limit = False

while guess != secret and not (out_of_limit):
    if attempts < limit:
        guess = int(input("G U E S S : "))
        attempts += 1
    else:
        out_of_limit = True

if out_of_limit == True:
    print("out of limit try again")
else:
    print("you won congo")
