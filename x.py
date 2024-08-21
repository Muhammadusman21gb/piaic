# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variable
height = int(input("enter height in meters"))
weight = int(input("enter weight in kg"))
BMI = weight / height**2
print(BMI)