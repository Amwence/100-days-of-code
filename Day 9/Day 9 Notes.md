# Dictionaries 

All dictionaries have 2 parts key and an associated value. 

- Key - Value

- Bug - An error in a program that prevents the program from running as expected. 

- Bug - An error in a program that prevents the program from running as expected

- Function - A piece of code that you can easily call over and over again. 

- Loop - The action of doing something over and over again.

To create a dictionary in python the syntax is `` {key: Value}``

Here is an example: 
```
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(programming_dictionary["Bug"])
```
The above code will call upon the programming dictionary at the key of ``"Bug"`` and return ``An error in a program that prevents the program from running as expected.``. 

*Note: the syntax for calling on a item in the dectionary is the name of the dictionary and then the key, so ``dictionary_name["key"]`` much like accessing an index for a list.  

## Adding an item to a dictionary

Start by calling upon the name of the diectionary at key equal to value. So for example:
```
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

programming_dictionary["New Key"] = " Something for the new key"
print(programming_dictionary)
```

This code will add the ``"New Key"`` to the dictionary, and then print the entire dictionary which should ahve the New Key addition.

## Creating a blank Dictionary

``dictionary = {} ``

## Wiping an existing dictionary

If you wanted to completely wipe an existing dictionary you could make the existing dictionary equal to an empty one.
``programming_dictionary = {}``
``print(programming_dictionary)``

## Edit items in a dictionary
``dictionary[key_name}]: "Change the thing in keyname to this"``

# Looping through a dictionary

```
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

for thing in programming_dictionary:
    print(thing)

```

This code will print the keys, even though I would have thought it would print the value. 

Instead use:
```
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

```

