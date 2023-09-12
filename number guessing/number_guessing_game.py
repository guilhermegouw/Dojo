"""
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
Too high
Too low
Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
"""
from random import randint


def guessing_game():
    number = randint(0, 100)
    while True:
        guess = input("Guess a number between 0 and 100: ")
        result = check_guess(guess, number)
        if result == "Just right!":
            print(result)
            break
        else:
            print(result)
        
def check_guess(guess, number):
    try:
        guess = int(guess)
    except ValueError:
        return "Please enter a number between 0 and 100."
    if guess < 0 or guess > 100:
        return "Please enter a number between 0 and 100."
    elif guess == number:
        return "Just right!"
    elif guess > number:
        return "Too high!"
    else:
        return "Too low!"

if __name__ == "__main__":
    guessing_game()
