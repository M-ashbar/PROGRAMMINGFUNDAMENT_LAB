#incorrect code
# x=5: #extra colon is used
# print(x)

#correct code
#store 5 in variable
# x = 5
#display the value of x
# print(x)

#incorrect code
# 1TEXT = "SSUET" #variable cannot start with number
# Number = 1
# #error : Addition is not possible because number and text are two data types
# print(Number + Text)

#correct code
#Store a string in text
# TEXT = "SSUET"
# #store an integar in number
# Number = 1
# print(Number , TEXT)#Display both values


#incorrect code
# a = b = 3 = 4 #cannot assign value to constant

#correct code
#assign 3 to both value
# a = b = 3
# #dispaly the value of a
# print(a)
# #display the value of b
# print(b)

# # perform arithmetic operator
# a = 2 % 2 + 2 * 2 - 2 / 2;
# #display final result
# print(a)


# perform multiplication and division 
# b = 3 / 2 + 5 * 4 / 3 ;
# #display result
# print(b)


#add 3 and 4 then assign the result of all variable
# c = b = a = 3 + 4 ;
# #display the result of all variable
# print(a)
# print(b)
# print(c)


# 	Write a program that calculates area of a circle A=πr^2. (Consider r = 50).

# store value of radius of circle
# r = 50
# 
# # store the value of pi
# pi = 3.14
# 
# # calculate the area of a circle
# A = pi*r*r
# 
# #display the calculatec area
# print("Area of a Circle",A)



# Write a program that performs the following four operations and prints their result on the screen. 
# a.	50 + 4
# b.	50 – 4
# c.	50 * 4
# d.	50 / 4

#store first number
# a = 50
# 
# #store second number
# b = 4
# 
# #add both number
# print("Addition = ",a+b)
# 
# # subtraction second number from first number
# print("Subtraction = ",a-b)
# 
# #divide the first number by second
# print("Multiplication = ",a*b)
# 
# #multiply both number
# print("Division = ",a/b)



# Write a Python program to convert height (in feet and inches) to centimeters.
# Convert height of 5 feet 2 inches to centimeters.
# •	First, convert 5 feet to inches: 5 feet × 12 inches/foot = 60 inches
# •	Add up our inches: 60 + 2 = 62 inches
# •	Convert inches to cm: 62 inches × 2.54 cm/inch = 157.48 cm


#store height in feet
feet = 5

#store the remaining height in inches
inches = 2

# convert feet in inches and add remaining inches
total_inches = feet * 12 + inches

#convert inches into centimeter
cm = total_inches *2.54

#display the height in cm
print("height in centimeter =", cm)





#import the math module to calculate the square root
import math

# Store the x1 and y1 value
x1 = 1
y1 = 2

#store the x2 and y2 value
x2 = 4
y2 = 6

# calculate the difference between x coordinates
dx = x2 - x1
# calculate the difference between y coordinates
dy = y2 - y1
#square both difference and add them
sum_squares = dx**2 + dy**2
#calculte the square root to find the distance
distance = math.sqrt(sum_squares)
#display the distance between two points
print('Distance between two points =',distance)