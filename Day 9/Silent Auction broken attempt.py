# This was done in replit so the clear import will need to be changed if not doing it in replit. I also didn't save the art so that won't work either.
#from replit import clear
#rom art import logo

#print(logo)
#HINT: You can call clear() to clear the output in the console. 

#Solution is convoluted and needs to be fixed. 

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