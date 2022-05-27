'''
Figured out where day 2 was broken, I forgot the parenthesis at the end of .lower() method. I'm suprised the linter didn't catch that. I now have a new issue.

The game when going to the stay function will sometimes just not work, or the player input function stalls and will take 2 inputs and the game will restart. 

I added a ton of print statements just to verify the code is going to each part, and I've also added I'm sure some redundant code which is adding to the problems.
I may need to clean it up sooner than later, I've also commented out all of the play again, because at some point it was just automagically going to play again, and 
entering an infinite loop. 

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
  print(logo)
  print("Game START")
  print("________________________________________")
  return dealer_hand, player_hand

# Deals initial hands with only 1 dealer card showing with a summary of the game state(current_status()), then asks player what to do next(player_choice())
def deal_cards():
    print("DEAL CARDS")
    print("________________________________________")
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
    print("Hit")
    print("________________________________________")
    player_hand.append(random.choice(cards))
    print("player hand hit", player_hand)
    if sum(player_hand)>21:
        print("PLAYER BUST")
        print("________________________________________")
        print(f"Sorry you BUST: {sum(player_hand)}\n")
        #play_again()

    else:
        player_choice()




#Stay function takes player's hand, and dealer's hand and if dealer hand is less than 17 adds cards and checks if they are either over 21, or more than the player.
def stay(player_hand, dealer_hand):
    print("STAY")
    print("________________________________________")
    if sum(dealer_hand)>=17 and sum(dealer_hand)<=21:
        if sum(player_hand)>sum(dealer_hand):
            print("Player Win STAY")
            current_status()

        else: 
            print("Player Lose Stay")
            current_status()


    while sum(dealer_hand)<17:
        dealer_hand.append(random.choice(cards))
        print(f"The Dealer has:{dealer_hand} and a total of {sum(dealer_hand)}")
        if sum(dealer_hand)>21:
            print("DEALER BUST")
            print("________________________________________")
            print(f"Player Hand: {player_hand}, total: {player_hand}\n",f"Dealer hand: {dealer_hand}, total: {sum(dealer_hand)} \n")
            print("You win!")
            #play_again()
            game_continue = False
            exit()

        elif sum(dealer_hand)> sum(player_hand):
            print("Dealer  WIN")
            print("________________________________________")
            print(f"Player Hand: {player_hand}, total: {sum(player_hand)}\n",f"Dealer hand: {dealer_hand}, total: {sum(dealer_hand)} \n", "Dealer Wins!")
            #play_again()
            game_continue = False
            exit()
            
        elif sum(dealer_hand) == sum(player_hand):
            print("ITS A DRAW")
            exit()
      
    
  

#Player Choice asks player if they want to hit or stay, and then passes either to the hit, or stay functions. 
def player_choice():
    print("PLAYER_CHOICE")
    print("________________________________________")
    current_status()
    print(player_hand)
    while sum(player_hand)<=21:
        print("playerhand less than")
        print("________________________________________")
        player_input = input("Do you want to hit or Stay? \n")
        print(player_input.lower())
        if player_input.lower() == 'hit':
            print("HITCHOICE")
            print("________________________________________")
            hit(player_hand)
            
        elif player_input.lower() == 'stay':
            print('STAYCHOICE')
            print("________________________________________")
            stay(player_hand, dealer_hand)

    else:
        print("play again player choice")
        exit()
        #play_again()



#Play again asks if player wants to play again if yes, passes to game start else exits.
#def play_again():
    #print("PLAY AGAIN")
    #state = input("Would you like to play again? \n Yes, or No?")
    #if state.lower() == 'yes':
        #game_Start(player_hand,dealer_hand)
        #deal_cards(player_hand,dealer_hand)
    #else:
        #exit()







# Current status prints to screen dealer hand, player hand, and the total of their cards. 
def current_status():
  print(f"Player Hand: {player_hand}\n",f"Dealer hand: {dealer_hand[0]}, X \n", f"The player is showing {sum(player_hand)}, and the Dealer is showing {dealer_hand[0]}.")
    



while game_continue:
  game_Start()
  deal_cards()
  
  