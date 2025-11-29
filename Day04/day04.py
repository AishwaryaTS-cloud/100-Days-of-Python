import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

# 1. User choice
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

# 2. Handle invalid choices before accessing the list
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose.")
else:
    # 3. Show user's move
    print(game_images[user_choice])

    # 4. Computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # 5. Determine the winner
    if user_choice == computer_choice:
        print("It's a draw.")

    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")

    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose.")

"""
What do you choose?
Type 0 for Rock, 1 for Paper, or 2 for Scissors:
2

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer chose:

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

You win!
"""