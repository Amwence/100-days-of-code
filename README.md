# 100-days-of-code
    Day 1- print() function 
        -print("your text here") 
            -outputs what was in quotes
            - quotes denotes that anything between them is not code and is known as a string and can includes spaces.
            -if you need quotes inside of your print statement you can do something like print("This is a 'quote' and alternatively you can switch the doubles on the outside for singles if needed so there would be double qoutes on the inside. /n is for a new line btw.")

        -print(variable)

        -Syntax Error: EOL while scanning string literal 
            -error on line while scanning string. 
       
        -Backslash N will create a new line 
            -\n and you do want gaps if you don't want a space in front of the next line. It would actually look like \nThis is a new line

        -Concactating lines is adding two together: print("this string " + "this String")
            - Would print this string this String . Notice the space in the first string at the end. 
            - can only concactate another string cannot + an integer or variable that has an integer stored. You have to use commas for stuff like that. 
            
        -len() will find the lenght of the input between the lines
        
        -Commands can be nested within eachother like:
            - print(len(input("What is your name?")))
        -variables: age = input("Age")  
        -
        -Not Technically in the lesson but I was fucking around and wanted to try it. int(input()) will take your input and store it as an integer. If you try and input a letter or anything other than an integer the program throws an error. I'm guessing in order to fix it I'd have to program debugging and input handling into the code. 

Day 2 notes- https://github.dev/Amwence/100-days-of-code/blob/47cdb8bb46ad855e1c202c1180a25b4d78496223/Day%202/Day%202

**Operator | Description | Example
_______________________________________
== | Returns if operand values are equal, and False otherwise | x==y #False x==z
!= | returns True if operands values are not equal, and False Otherwise | x!=y #True x!=z #False