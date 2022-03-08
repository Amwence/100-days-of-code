'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

'''

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

def randoname(names):
  names_list = []
  for name in names:
    names_list.append(name)
    continue 
  return random.choice(names_list)

print("The person paying today is: ", randoname(names))

# have since found out that the .split method saves them into a list.
# I did not need the names_list list. I basically took a list and appended using a for loop into another list.
#I also missed the part where they said not to use the .choice method.

#Their solution:

num_items = len(names)
rand_choice= random.randint(0, numb_items - 1)
person_who_will_pay = names[rand_choice]
print(person_who_will_pay + " is going to buy the meal.")