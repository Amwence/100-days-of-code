#Day 2 Code
#1/12/2022
# Understanding Data Types and Manipulating Strings
 
 #Data Types

 #String

"123"
print("123"+"345")

print("Hello"[4])
#Pulls an element from a string and starts from 0 code above will produce H
#It is called subscripting.

# Integer
# Is numbers that can be used to do Math
# If you want large numbers with commas in them in your code you replace with underscore.
#123,321,000 is 123_321_000. The comma is a seperator and would not work the way you expect. 

print(123_321_000)
print(1+2+3+4)

#Float
#Short for floating point number or a decimal value. So 3.14 or something like that. 

3.14159

#Boolean

True
False

num_Char = len(input("what was your name? "))

print(type(num_Char))

print(type(int((input("Type \n")))))
# if you dont know what kind of code use a type check.

new_num_Char = str(num_Char)
print(new_num_Char)

#different data types
boolean = bool(1+1)
string = str("Yo mama")
integer = int(7)
floating_Point = float(3.25)

print("Boolean: \n")
print(boolean)
print(type(boolean))

print("String: \n")
print(string)
print(type(string))

print("Integer: \n")
print(integer)
print(type(integer))

print("Floating Point/Decimal: \n")
print(floating_Point)
print(type(floating_Point))

#so Different types are float(Floatingpoint) int(integer) str(string) bool()

# Mathematics
# Different operators are + - * /. Addition, Subtraction, Multiplication, and Division. ** is for exponents 2**3 is two to the power of 3

print("2+4/2= ", end= "")
print(2+4/2)
print()

print("2*5= ", end= " ")
print(2*5) 
print()

#Division defaults to a float type 
print("245= ", end=" ")
print(2/4)
print()



print("3-15= ", end=" " )
print(float(3-15))
print()

print("Two to the Power of Three: 2**3 ")
print(2**3)
print()

# Uses PEMDAS for order of priority. 
#Paranethesis ()
# Exponents ** 
# Multiplication */ whichever is farthest to the left hapens first
# Division / * Whichever is farthest to the left happens first
# Addition + 
# Subtraction -

print(3*3/3-3) # happens from left to right because multiplication and division has the same priority.
print(3*3+3/3-3) #outputs to 7 because of PEMDAS