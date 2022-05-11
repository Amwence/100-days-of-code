# Function's with output

You can have functions return output where it overwrites the function and saves the operation as a variable. You do this by using the ``return`` keyword, and assigning the function to a variable. 
for example:
```
def myfunc(param1,param2):
    return param1+param2

results = myfunc(3, 10)
print(results)
```
The result should be 13 printed to screen. It takes the function in results passes the arguments through the function and saves the return statement into results. 

# Docstring

In programming, a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code. In python this would be done using 3 quotation marks immediately after a function. This is used when you hover over it in a code editor it will tell you what it does. It's for if you are using a function over and over and don't remember what it does you can create a docstring to explain it without having to comment the code everytime it is used. 
For example

```
def myfunc(param1,param2):
    """ This function adds two numbers together """
    return param1+param2

results = myfunc(3, 10)
print(results)
```