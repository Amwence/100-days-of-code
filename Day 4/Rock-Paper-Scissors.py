'''
Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
'''

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

import random

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))

import random

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))

def computer_Output():
    rpc = random.randint(0,2)
    return rpc

dictionary = {rock:0, paper:1, scissors:2}
key_list= list(dictionary)
computer = computer_Output()

if player_input == 0 and computer == 1:
  print(" Sorry you Lose! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 0 and computer== 0:
  print("It's a Draw!")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 0 and computer == 2:
  print(" You Win! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")

if player_input == 1 and computer == 2:
  print(" Sorry you Lose! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 1 and computer == 1:
  print("It's a Draw!")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 1 and computer == 0:
  print(" You Win! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")

if player_input == 2 and computer == 0:
  print(" Sorry you Lose! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 2 and computer== 2:
  print("It's a Draw!")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")
elif player_input == 2 and computer == 1:
  print(" You Win! ")
  print(f"You chose: {key_list[player_input]}")
  print(f"The computer chose: {key_list[computer]}")

else:
  print("Incorrect input, Goodbye!")