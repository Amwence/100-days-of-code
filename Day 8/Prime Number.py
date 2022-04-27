#Write your code below this line 👇

def prime_checker(number):
  divisible = []
  # cycles through numbers from 1 to number selected and divides them by eachother to see if any have a remainder.
  for x in range(1, number, 1):
    y = number%x
    
    # adds divisible numbers to list
    if y == 0 and x != number and x != 1:
      divisible.append(x)
   # checks if list is not empty for Not Prime 
  if divisible != []:
    print("divisible by: ", divisible,"\n It's not a prime number.")
      
    #Checks if list is empty for Prime
  elif divisible == []: 
    print("It's a prime number.")
  
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



