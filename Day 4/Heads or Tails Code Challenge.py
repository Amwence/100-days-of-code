# Virtual coin toss program.
# User random numbers to simulate a coin toss. 

import random

def coin_toss():
    result= random.randint(1,100)
    return result

interaction = input("Ready to flip the coin? Y/N: ")
try:
    if interaction.lower() == 'y':
        if coin_toss() > 50:
          print("Heads")
          
        else:
          print("Tails")
          
    elif interaction.lower()=='n': 
        print("Goodbye")

except TypeError:
    print("Sorry Wrong input")

except ValueError:
    print("Sorry Wrong input")

# Error handling not working. Look into this later. 