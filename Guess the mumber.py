import random
n=random.randint(1,100)
m= int(input("Guess a number between 1 to 100:"))
if n==m:
    print("You Guessed Right!!!")
else:
    print("WRONG-HAHA LOSER")
    print("Computer has selected:",n)