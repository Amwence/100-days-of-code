# this is a comment these are some of the commands we learned.
# print command both single and double qoutes and \n for new line. 
# + to add strings together


print("Hello World")
print('Hello \nDude!' + "\nYo Wassup")
print('Why would anyone use "" Double quotes gross :( ' )

#Input
# you can nest things within eachother like in the line with input
# It will display What is your name then when the input is received it
# then display hello followed by the input. 
#thonny is a tool that will allow you to see how code is executed step by step. 
#
print('Hello ' + input('Who are you? \n'))

nickname = len(input("What is your Nickname?"))
that = "That has "
letters = ' letters in it'
print (that , nickname , letters)

# Something I was having trouble with was I could not take a length and 
#show it within a string. I figured out if you use commas you'd be fine
# as you can see from the code above I tried seperating everything into
#variables first and it didn't work. Still was a number nested in a string
# with the + sign which does not work. Commas were the way to go. 

#This is a comment this was also in the lesson.
#the len() command will show the lenght of a string so the question
# how to print what is your name and print the length of the name

print(len(input("What is your first name? \n")))

#Assigning Variables
#Input always takes a string so to get a number so you can perform
#maths on an input you need to nest it in the int(input()) command


first_Name = input("What is was your First Name again???? \n")
last_Name = input("What is your Last Name? \n")
age = int(input("How old are you? \n"))
length_Last = len(last_Name)
length_First = len(first_Name)

#### this is just something I was fucking with no idea if it will work.
#int(age)
#int(length_Last)
#int(length_First)
##### It doesnt work
print("This is your lucky Number: ") 
print(length_First + age /2 * length_Last)
print("Hello")
print(first_Name +" "+ last_Name)

#Code challenge Below program that switches variables

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = b
d = a

a = c
b = d



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

