import os
clear = lambda: os.system("cls")

from art import logo, vs
from game_data import data
import random

def Max_Follower_Count(option_A, option_B):
    if option_A["follower_count"] > option_B["follower_count"]:
        max = "a"
    else:
        max = "b"

    return max

def Formate_Dict(dict):
    return(f"{dict['name']}, a {dict['description']}, from {dict['country']}")

def Game():
    score = 0
    option_A = random.choice(data)

    clear()
    print(logo)
    loop = True
    while loop:
        option_B = random.choice(data)
        while option_A == option_B:
            option_B = random.choice(data)

        max_follower = Max_Follower_Count(option_A, option_B)

        print(f"Compare A: {Formate_Dict(option_A)}.")
        print(vs)
        print(f"Against B: {Formate_Dict(option_B)}.")
        
        your_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()
        print(logo)
        
        if your_answer == max_follower:
            score += 1
            print(f"You're right! Current score: {score}.")
            option_A = option_B
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            loop = False

play = True
while play:
    Game()
    play_again = input("Press 'Enter' key to play again or type 'e' to exit the game: ").lower()
    if play_again == "e":
        play = False
        clear()