import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

icons = [rock, paper, scissors]


me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer = random.randint(0,2)

if me >= 0 and me < 3:
    print(icons[me])
    print("Computer chose:")
    print(icons[computer])

    if me == 0:
        if computer == 0:
            print("It's a draw")
        elif computer == 1:
            print("You lose")
        elif computer == 2:
            print("You win!")
    elif me == 1:
        if computer == 0:
            print("You win!")
        elif computer == 1:
            print("It's a draw")
        elif computer == 2:
            print("You lose")
    elif me == 2:
        if computer == 0:
            print("You lose")
        elif computer == 1:
            print("You win!")
        elif computer == 2:
            print("It's a draw")
    else:
	    print("You typed and invalid number, you lose!")
else :
     print("You typed and invalid number, you lose!")