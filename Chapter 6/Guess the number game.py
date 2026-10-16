# Mini Project – Guess the Number Game
# Concepts Used: while loop and user input.
# Sample Run:
# Guess a number between 1 and 10: 4
# Wrong guess! Try again.
# Guess again: 7
# Congratulations, Saumya! You guessed it right

#Step 1  generated a random number between 1 and 10
import random

secret_number= random.randint(1,10)
name= "heer khan"

guess= int(input("Guess a number between 1 and 10:"))

while guess!= secret_number:
        print("Wrong guess, Try again!")
        guess= int(input("Guess Again:"))

print(f"congratuation {name} , You guessed it right:")

