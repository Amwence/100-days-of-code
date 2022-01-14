# Tip Calculator

print("Welcome to the tip calculator ")

#Total_ tip =total price of bill * percentage of tip

total_Bill = input("What was the bill total? \n")

total_Bill = float(total_Bill)

tip_Percentage = input("What percentage of tip did you want to leave (Please do not include a '%' symbol only numbers)")

tip_Percentage = float(tip_Percentage)

tip = tip_Percentage / 100

tip *= total_Bill


print(f"The tip would be: $ {round(tip,2)} ")

#Things learned is that you cannot use the float() tag inside the input field when applying to variable. I had to do it seperate. Not sure if done incorrectly, or if there is something I'm not understanding. 