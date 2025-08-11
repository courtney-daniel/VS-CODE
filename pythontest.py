# print("Hello World!")
# This script prints "Hello World!" to the console.
# It is a simple demonstration of a Python script.  
# print("Hello World!")

import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer!")

guess_the_number()

#adding this line as I learn how to commit to a new branch on github
#adding another line to test commit functionality
