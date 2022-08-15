# n(n-1)/2 is the math for how hard it is to manage keys. N is the number of people who have the keys, and how many people you need to manage having those keys. 
#Quickly gets out of hand when doing the math.

key = int(input("How many people will need keys?"))
for number in range(key+1):
  n = number
  math = number*(number-1)/2
  print("Number of people who need keys: ",n, " ",  "here is the number of keys you'll have to mangage: ", math)