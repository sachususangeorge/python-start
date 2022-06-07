import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number=random.randint(1,10)
isguessright = False
while isguessright !=True:
    guess=input("Guess a no between 1 and 10: ")
    if int(guess)==number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isguessright=True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))