# from replit import clear
import os
clear = lambda: os.system('cls')

from art import logo
#HINT: You can call clear() to clear the output in the console.

acution = {}
loop = True
while loop:
    # Show the logo
    print(logo)
    print("\n")

    # Ask for the name
    name = input("What is your name?: ")

    # Ask for the bid price
    bid = input("What is your bid?: $")

    # Add the name and bid to the auction dictionary    
    acution[name] = bid

    others = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if others == "yes":
        loop = True
    else:
        loop = False

    # Clear the screen at the end of each loop.
    clear()
    
# Selecting the max bidder.
for key in acution:
    max_bid = 0
    bidder_name = ""
    if int(acution[key]) >= max_bid:
        bidder_name = key
        max_bid = acution[key]

# Show the max bidder.
print(f"The winner is {bidder_name} with a bid of ${acution[bidder_name]}")