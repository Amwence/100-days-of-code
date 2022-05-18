'''
Currently game gets hung up on the player choice function. Need to find fix. 
Code is also a bit wonky with all the functions calling other functions. There is definitely a better way to do this and make it more readable.
Need to fix code, then maybe find a way to cut out things that aren't needed, like current status, or update current status so it can be called
instead of having all of the print statements within the functions. Make it so that current status has all the print statements in it, but gives
different outputs depending on what function you are in, and what output you want. Also possibly find a way to clear the screen so it doesn't seem 
so cluttered. An ace can usually be either an 11 or a 1 maybe add that in at a later date, along with the split option if you have two of the same 
card. 

'''


import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand= []
player_hand= []
game_continue= True

#Clears players hand to start new game
def game_Start():
  dealer_hand= []
  player_hand= []
  return dealer_hand, player_hand

# Deals initial hands with only 1 dealer card showing with a summary of the game state(current_status()), then asks player what to do next(player_choice())
def deal_cards():
  if len(player_hand)<=0:
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    
    print(f"Player Hand: {player_hand}\n",f"Dealer hand: {dealer_hand}")

    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    
    current_status()
    
    return player_hand, dealer_hand, player_choice()


# Hit function adds 1 card to player hand if their total is larger than 21 they bust and asks to play again. If they aren't over 21 goes back to player_choice()
def hit(player_hand):
  player_hand.append(random.choice(cards))
  print("player hand hit", player_hand)
  if sum(player_hand)>21:
    print(f"Sorry you BUST: {sum(player_hand)}\n")
    play_again()

  else:
    player_choice()




#Stay function takes player's hand, and dealer's hand and if dealer hand is less than 17 adds cards and checks if they are either over 21, or more than the player.
def stay(player_hand, dealer_hand):
  while sum(dealer_hand)<17:
    dealer_hand.append(random.choice(cards))
    print(f"The Dealer has:{dealer_hand} and a total of {sum(dealer_hand)}")
    if sum(dealer_hand)>21:
      print(f"Player Hand: {player_hand}, total: {player_hand}\n",f"Dealer hand: {dealer_hand}, total: {sum(dealer_hand)} \n")
      print("You win!")
      play_again()

    elif sum(dealer_hand)> sum(player_hand):
      print(f"Player Hand: {player_hand}, total: {sum(player_hand)}\n",f"Dealer hand: {dealer_hand}, total: {sum(dealer_hand)} \n", "Dealer Wins!")
      play_again()
      
  pass
  

#Player Choice asks player if they want to hit or stay, and then passes either to the hit, or stay functions. 
def player_choice():
  current_status()
  print(player_hand)
  if sum(player_hand)<21:
    player_input = input("Do you want to hit or Stay? \n")
    if player_input.lower == 'hit':
      hit(player_hand)
    else:
      stay(player_hand, dealer_hand)
  else:
    play_again()



#Play again asks if player wants to play again if yes, passes to game start else exits.
def play_again():
  state = input("Would you like to play again? \n Yes, or No?")
  if state.lower() == 'yes':
    game_Start()
    deal_cards()
  else:
    exit()







# Current status prints to screen dealer hand, player hand, and the total of their cards. 
def current_status():
  print(f"Player Hand: {player_hand}\n",f"Dealer hand: {dealer_hand[0]}, X \n", f"The player is showing {sum(player_hand)}, and the Dealer is showing {dealer_hand[0]}.")
    



while game_continue:
  game_Start()
  deal_cards()