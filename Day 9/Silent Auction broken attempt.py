from replit import clear
from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console. 
total_bids ={}
value=[] 

name = input("What is your name?")
bid = float(input("What is your bid?"))
def bidding(name, bid):

  
 
  total_bids = {

    "name": name,
    "bid": bid,
    }
  continue_bidding = input("Are there anymore people bidding? yes, no \n")
  total = 0
  if continue_bidding.lower() == 'yes':
    clear()
    bidding(name,bid)
  else:
    clear()
    for key in total_bids:
      if total < total_bids[key["bid"]]:
        total = total_bids[key["bid"]]
        value = [key]
      elif total == total_bids[key["bid"]]:
        value.append[key]
      else:
        continue
      return value
bidding(name, bid)
if len(value) > 1 :
  print("We have a draw, ", value, "both win.")

else:
  print("The winner is ", value)