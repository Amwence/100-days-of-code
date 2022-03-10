'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

def height_addition(student_heights):
  #for num in student_heights:
  total = sum(student_heights)
  return total

print(f"list = {student_heights}")
print(f"sum = {height_addition(student_heights)}")

average = height_addition(student_heights) // len(student_heights)

print(f"The average among {student_heights} ", f'is {average}')

#option 1 not allowed because I used sum and len functions. 
# I need to learn to read the instructions

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


for num in range(0,len(student_heights)):
  print(student_heights[num])
  total = student_heights[num] + student_heights[0]
  

print(f"list = {student_heights}")
print(f"sum = {total}")

average = total // len(student_heights)

print(f"The average among {student_heights} ", f'is {average}')