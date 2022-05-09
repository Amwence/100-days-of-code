from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    for bidder in bidding_record:
        bid
while not bidding_finished:
    name = input("What is your name")
    price = int(input("what is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? 'yes' or 'no'")
    if should_continue.lower() =="no":
        bidding_finished = True
    elif should_continue.lower() == "yes":
        clear()
