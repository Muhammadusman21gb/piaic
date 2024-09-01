#  #- Convert a given number of seconds into minutes and seconds using variables.
# #inputNumber = int(input("enter your number"))
# #result = inputNumber * 60
# #print(result)
# #inputNumber = int(input("enter your number"))
# #result = inputNumber / 60 
# #print(result)
 
# def add(num3,num4):
#     num1 = 20
#     num2 = 40
#     result = num3 + num4
#     print(result)
#     def divide():
#         num3 = 20
#         num4 = 80
#         result2 = num3 % num4
#         print(result2)
#     divide()
# add(10,30 )
# def add (num1,num2):
#     result = num1 + num2
#     return result
# output = add(50,30)
# finalOutput = add(output,70)
# print(finalOutput)

def Calculate_age(ageYear:int)->int:
    currentYear:int = 2024
    return currentYear - ageYear
ageYear:int = int(input("Enter Age Year: "))
age:int = Calculate_age(ageYear)
print("Your age is: ", age)    
