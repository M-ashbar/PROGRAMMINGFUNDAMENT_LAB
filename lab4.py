# is incorrect. We only need a = 500
# a = 500,b,c; 
# the remaining code is incorrect
# a = 500,b,c;
# if (a => 400):
#     b = 300
#     c = 200
#     print("value is:",b,c)


# store 500 in variable a
# a = 500
# # check a is greater or equal to 400
# if a >= 400:
#     b = 300 #store 300 in variable b
#     c = 200 #store 200 in variable c
#     #display result
#     print("value is:",b,c)

#incorrect code
# error because variable cannot start with &
# &number = eval(input("Enter an Integar:"))
# print (type(number))
# # in if statement colon(:) is missing
# if number % 5 == 0
#     print("HIFIVE")
# # also in else statement colon(:) is missing
# else
#     print("No Answer")
#     
    
#ask user to enter an integar 
# number = eval(input("Enter an Integar:"))
# # display data type of number
# print (type(number))
# # check number is divisible by 0
# #run if remainder is zero 
# if number % 5 == 0:
#     print("HiFive")
# else:
# # run if the remainder is not zero
#     print("No Answer")


#incorrect code
# Colons : are missing after all if and elif conditions.
# No score value has been given to variable
# Condition should be checked from (Highest to Low )
# otherwise score 70,80,90 will satisfy score 60.0
# if score >= 60.0
#     grade = 'D'
# elif score >= 70.0
#     grade = 'C'
# elif score >= 80.0
#     grade = 'B'
# elif score >= 90.0
#     grade = 'A'
# else:
#     grade = 'F'


# correct code
#take input from User
# score = float(input("Enter your Score :"))
# # check score if 90 or above
# if score >= 90.0:
#     grade = 'A'
# # check score if 80 or above
# elif score >= 80.0:
#     grade = 'B'
# # check score if 70 or above
# elif score >= 70.0:
#     grade = 'C'
# # check score if 60 or above
# elif score >= 60.0:
#     grade = 'D'
# # check score if below 60
# else:
#     grade = 'F'
# # Display the result
# print("The grade is :" , grade)

# store mushroom in topping variable
# requested_topping = "mushroom"
# # check if topping is not anchovies
# if requested_topping != "anchovies":
#     print("Hold the anchovies")
# Display if condition is true


#store 3 in num
# num = 3
# # check if number is positive or zero
# if num >= 0 :#display if condition is true
#     print("Number is positive or Zero")
# else:  #display if condition is false
#     print("Number is Negative")


#store 15 in age variable
# age = 15
# 
# # check age if below 4
# if age < 4:
#     price = 0
# #check if age is below 18
# elif age < 18:
#     price = 1500
# #if previous condition is not true run this
# else:
#     price = 2000
# 
# # Display admission cost
# print("Your Admission cost is Rs" + str(price) + '.')



# Any integer is input through the keyboard.
# Write a program to find out whether it is an odd number or even number.

# take input from user 
# num = int(input("Enter an Integar :"))
# #check if remainder is 0
# if num % 2 == 0:
# # Display if number is even 
#     print("The Number is Even")
# else:
# # Display if number is odd
#     print("The Number is Odd")



# 
# . Write a program that asks for years of service and qualification
# from the user and calculates the salary as per the following table:
# Years of Service	Qualifications	Salary
# >= 10	Masters	150,000
# >= 10	Bachelors	100,000
# < 10	Masters	100,000
# < 10	Bachelors	70,000


# Take Servie year from user
# YOS = int(input("Enter your Service years"))
# # Take qualifiation from user
# Qualification = input("Enter your Qualification")
# 
# # chek YOS and Qualifiation
# # salary for 10+ years and masters 
# if YOS >= 10 and Qualification == "Masters":
#      Salary = 150000
# # salary for 10+ years and Bahelors
# elif YOS >= 10 and Qualification == "Bachelors":
#      Salary = 100000
# # salary for less than 10years and masters
# elif YOS < 10 and Qualification == "Masters":
#      Salary = 100000
# # salary for less than 10years and bahelors
# elif YOS < 10 and Qualification == "Bachelors":
#      Salary = 75000
# # Yos and Qualification is not match
# else:
#     salary = 0
# #Display salary
# print("your salary is Rs :", Salary)
#      
     
     



# 
# 3. Write an if-elif-else chain that determines a person’s stage of life,
# take input value for the variable age, and then apply these conditions:


#Take person stage from user
Person_Stage = int(input("Enter your Age : "))
# apply this condition to check person stage of life
if Person_Stage <= 2:
    print("The person is Baby")
elif Person_Stage <= 4:
    print("The person is Toddler")
elif Person_Stage <= 13:
    print("The person is Kid")
elif Person_Stage <= 18:
    print("The person is teenager")
elif Person_Stage <= 65:
    print("The person is Adult")
elif Person_Stage >= 65:
    print("The person is elder")








































