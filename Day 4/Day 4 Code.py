#You can add modules by using the import command. You can get PRNG by doing import random

import random

random_d20 = random.randint(1,20)

print("This is a roll of a d20: ", random_d20) # should print a random integer between 1 and 20. Is inclusive to both numbers.

#Random Floating point numbers.

random_float = random.random()
print(random_float) #should output something between 0.0 and 1.0 not includeing 1.0

#Creating random floating point between two integers

random_float_range = random.random() * 5
print(random_float_range) # Would print from 0.0 to 5.0 not including 5.

#Lists are a special variable that is ordered and contains multiple values.

list = [1,"String",True,{'Dictionary'},('Tuple1','Tuple2'),["another","list"]]
print(list) #Prints the list
print(list[5]) # prints the 5th item in list. List starts at 0.
print(list[4][0]) #prints the item in that index (Tuple1,Tuple2) and the index within that. So Tuple1.
