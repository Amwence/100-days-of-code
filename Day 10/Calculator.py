from art import logo

print(logo)

def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def division(num1, num2):
  return num1 / num2

def multiplication(num1, num2):
  return num1 * num2 

operations = {
  "+": addition,
  "-": subtraction,
  "/": division,
  "*": multiplication,
}

num1 = int(input("What is the first number? \n"))

for symbol in operations:
  print(symbol)

operator = input("What operation do you want to perform? (+,-,/,*)\n")

num2 = int(input("what is the second number? \n"))

result = operations[operator]