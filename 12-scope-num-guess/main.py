import random
from art import logo

# Global variables
EASY_LIVES = 10
HARD_LIVES = 5

# TODO-1: Import the logo from art.py and print it at the start of the game.
def print_logo():
    print(logo)

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        lives = EASY_LIVES
    else:
        lives = HARD_LIVES
    return lives


def play_game():
    print_logo()
    lives = set_difficulty()
    number = random.randint(1, 100)
    print(f"Psst, the correct answer is {number}")

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            lives -= 1
        elif guess < number:
            print("Too low.")
            lives -= 1
        else:
            print(f"You got it! The answer was {number}.")

        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
            
play_game()

