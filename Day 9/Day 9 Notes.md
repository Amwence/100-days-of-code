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
``dictionary[key_name]: "Change the value in keyname to this"``

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

## Nesting dictionaries

You can nest a dictionary into both a list and another dictionary.
```
nested_list = [
    {
        "key": "value",
        "different_key": "value",
        "number_value": 2
    }
]

nested_dict = {
    {
        "dict_key" : "value"
        "dict_list" : [val1,val2,val3]
    }
}
print(nested_list)
print(nested_dict)
```

Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
