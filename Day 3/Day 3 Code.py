water_Level = input("How much whater is there? ")
water_Level = int(water_Level)

if water_Level > 80:
  print("Drain the water")
  

else:
  print("You're still ok, keep going. ")


#Nested if statements

print("welcome to the rollercoaster")
height = int(input("What is your height in cm"))

if height >= 120:
  print("you can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7 ")
  else:
    print("Please pay $12")

else:
  print("Sorry, you have to grow taller before you can ride. ")

#My code
water_Level = input("How much whater is there? ")
water_Level = int(water_Level)


if water_Level > 80:
  print("Drain the water")
elif water_Level == 80:
  print("You can stop now")

else:
  print()

  
