import random
import os
clear = lambda: os.system("cls")
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def SetDifficulty():
    """Accourding to the level of game selected by the user, it will return the number of attempts left."""

    game_level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if game_level == "easy":
        attempts = EASY_LEVEL_ATTEMPTS
    else:
        attempts = HARD_LEVEL_ATTEMPTS
    return attempts
    
def Game():
    """It starts the Number Guessing Game."""

    clear()
    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    attempts_left = SetDifficulty()
    while attempts_left != 0:
        print(f"\nYou have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Too high.")
            attempts_left -= 1
        elif guess < answer:
            print("Too low.")
            attempts_left -= 1
        else:
            print(f"You got it! The answer was {answer}.")
            return

        if guess != answer and attempts_left != 0:
            print("Guess again.")

    if attempts_left == 0:
        print("You've run out of guesses, you lose.")

play = "yes"
while play == "yes":
    Game()
    play = input("\nDo you want to play it again? Type 'yes' to play again or 'no' to exit the game: ").lower()
    if play != "yes":
        clear()