## Day 4 code Randomisation and Python Lists
<br></br>

## Randomization:

<p>Python uses the Mersenne Twister. Which is a qseudorandom number generator (PRNG). 
</P>

In order to use the random number module we first need to ``import`` it using the ``import random`` command. After the **method** has been imported you can use the method commands to create different random integers, floating points, sequences, etc. For more information try checking the
[Random module](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) for more information.
<br></br>
<p> 
What is a module? In Python, <b>Modules</b> are simply files with the ".py" extension containing Python code that can be imported inside another Python program. In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application. <br></br>

We were quickly shown how to create our own module's to import by creating a new file called my_module.py, and then creating a variable called pi within that file. We then would ``import my_module`` and could then call the variable by ``my_module.pi`` so we used the command ``print(my_module.pi)`` and it called that variable. 
</p>


### Random Integers:

``import random`` Imports the random module and allows you to use the different methods.<br>
``random.randrange(start,stop,step)`` Returns a randomly selected integer from range(start,stop,step). This raises a ValueError if Start>Stop.<br>
``random.randint(a,b)`` Returns a random integer between a and b (both Inclusive). This also raises a value error if a>b.<br>

### Random Floating Point Numbers:

``random.random()`` Returns the next random floating point number between [0.0 to  1.0). Not inclusive, and does **not** include 1.0.<br>
``random.uniform(a,b)`` Returns a random floating point N such that *a<=N<=b* if *a<=b* and *b<=N<=a* if *b<a* . <br>

### Random Sequence:
``random.shuffle(x)`` This is used to shuffle the sequence in place. A sequence can be any list/tuple containing elements. <br>
``random.choice(seq)`` This is a widely used function in practice, wherein you would want to randomly pick up an item from a List/Sequence.
``random.sample(population,k)`` Returns a random sample from a sequence of length k

## Commands:
Integers:<br>
``import random``<br>
``random.randrange(start,stop,step)``<br>
``random.randint(a,b)``<br>
<br>
Floating point:<br>

``import random`` <br>
``random.random()`` <br>
``random.uniform(a,b)``<br>
<br>
Sequence/List:

``import random``<br>
``random.shuffle(x)``<br>
``random.choice(seq)``<br>
``random.sample(population,k)``<br>  

## Lists: 

Lists in python are mutable meaning they can be changed by reassigning the list, they can be blank, or changed by using methods. Lists are created by assigning a name of the list and setting it equal to ``[]`` seperated by ``,`` commas. A blank list can be changed by either reassigning the values in a list with another statement adding the values to a list with the same name, essentially overwriting it, or by: 

``name_of_list = [value1,value2,value3]`` Creates a list<br>
``name_of_list[index]`` How you would call on a specific part of a list<br>
``name_of_list[initial:end:index_jump]`` List slicing is when you select a range from a list. It does not include the end index, so if you chose range [1:5:1] it would display 1-4 and increment by 1. Much like how the ``range(start:stop:index_jump)`` function works.  <br>
``name_of_list.append(value)`` Appends to the end of a list.<br>
``name_of_list.insert(index_value, value)`` Will insert the value where the index indicates. Starts at 0, and negative indeces would be the end of the list, so -1 would be the last item in a list -2 would be the second to last and so on. When inserting at a certain point in the list it takes the current value in that index and shifts it and everything else down. <br>
``name_of_list = [value1,[value2,value3],value4]`` You can nest lists within other lists. In this example if you looked at the index of 1 it would be both value 2 and 3. <br>
``name_of_list.sort()`` Sorts a list. <br>
``name_of_list.pop([index])`` Removes an item from that index of a list.<br>
``name_of_list.clear()`` Deletes all contents of a list.
``name_of_list.extend(value1)`` Add the elements of a list (or any iterable), to the end of the current list. Only takes one argument/value, but can be used to add more than one value to a list.<br>
Example:<br> 
``name_of_list.extend([value1,value2,value3,value4])`` while trying this with append would put all the values into that index as another list. Extend will add each of those values to the end of the list you are working with giving them their own indeces. Whereas append would put all those values as a list at that index. 
<br>
*Note: List values start at index 0, however when starting at the end of a list the values start at -1.*
<br>
<br>
```````
#Creating a list
list = [1,2,3,4]
print(list)

#Adding things to list
list = [1,2,3,4]

list.append(5) #adds the number 5 to the end of the list
print(list)
list.insert([0],0) #adds a 0 to the beginning of the list which is index 0
print(list) #prints [0,1,2,3,4,5]

#Working with lists
list = [1,2,3,4]
print(list[3]) # prints the item at the index 3 of the list, which would be 4
list_dif = ['a',['b','c'],'d','e']
print(list[-3]) # would print [b,c] because you can nest lists inside eachother and that index has both those values. 
```````
## Commands:<br>
``name_of_list.insert(index_value, value)``<br>
``name_of_list.append(value)``<br>
``name_of_list = [value1_index0,value2_index1,value3_index2]``<br>
``name_of_list[index]``<br>
``name_of_list[start:stop:index_jump]``<br>
``name_of_list.sort()``<br>
``name_of_list.clear()``<br>
``name_of_list.pop([index])``<br>
``name_of_list.extend(value)``<br>
``name_of_list.extend([value1,value2,value3])``<br>

## New Commands
``string.split(argument)``<br>
example:<br>
```
txt = "Welcome to the jungle"
x = txt.split()
print(x)

txt_input = input("Input text her separated by a , comma then a space :")
list = txt_input.split(",")
print(list)
```
