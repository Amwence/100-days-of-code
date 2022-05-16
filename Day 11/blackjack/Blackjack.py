import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand= []
player_hand= []
game_continue= True

def game_Start():
  dealer_hand= []
  player_hand= []
  return dealer_hand, player_hand


def deal_cards():
  if len(player_hand)<=0:
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    
    print(f"Player Hand: {player_hand}\n",f"Dealer hand: {dealer_hand}")

    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    
    current_status()
    player_choice(player_input)
    return player_hand, dealer_hand


def hit(player_hand):
  player_hand.append(random.choice(cards))
  
  if sum(player_hand)>21:
      print(f"Sorry you BUST: {sum(player_hand)}\n")
      play_again()
  
  elif sum(player_hand)<21:
    player_choice()
      



def stay(player_hand, dealer_hand):
  while sum(dealer_hand)<17:
    dealer_hand.append(random.choice(cards))
    print(f"The Dealer has:{dealer_hand} and a total of {sum(dealer_hand)}")
    if sum(dealer_hand)>21:
      print(f"Player Hand: {player_hand}, total: {player_hand}\n",f"Dealer hand: {dealer_hand}, total: {sum(dealer_hand)} \n")
      print("/n/n/n You win!")
      play_again()
      
  pass
  

def player_choice():
  global player_input
  current_status()
  player_input = print(input("Do you want to hit or Stay?"))
  if player_input.lower == 'hit':
    return hit(player_hand)
  else:
    stay(player_hand, dealer_hand)



def play_again():
  state = input("Would you like to play again? \n Yes, or No?")
  if state.lower() == 'yes':
    return game()
  else:
    return







def current_status():
  print(f"Player Hand: {player_hand}\n",f"Dealer hand: {dealer_hand[0]}, X \n", f"The player is showing {sum(player_hand)}, and the Dealer is showing {dealer_hand[0]}.")
    



while game_continue:
  game_start()
  deal_cards()
  