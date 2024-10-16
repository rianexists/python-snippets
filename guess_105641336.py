from random import randrange

magic = randrange(1,11)

while True:
    guess = int(input("Please guess a number between 1 and 10: "))
    if guess == magic:
        print("You guessed it. Well done!")
        break
    elif guess > magic:
        print("Lower")
    elif guess < magic:
        print("Higher")