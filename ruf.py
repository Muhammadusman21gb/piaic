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
# print(finalOutput
    


# marks = int(input("enter your marks :"))
# if (marks >= 90 ):
#     print("A+ grade")
# elif (marks >= 80 and marks <= 89):
#     print("A grade")
# elif (marks >= 70 and marks <= 79):
#     print ("B+ Grade")
# elif (marks >= 60 and marks <= 69):
#     print("B grade")
# elif (marks >= 50 and marks <= 59):
#     print("c grade")
# elif (marks >= 40 and marks <= 49):
#     print("D grade")
# elif (marks >= 20 and marks <= 39):
#     print("F grade ,Fail")
# elif (marks >= 5 and marks <=19):
#     print("programme to wr gya")
# elif (marks >= 1 and marks <= 4):
#     print("too to gya son")
# else:
#     print("error")
##############################          PALINDROME:::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::
# list1 = [ 1, 2 ,3 ,4 ,5 ,4,3 ,2 ,1]
# 
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if (list1 == copy_list1 ):
#     print("palindrome")
# else:
#     print("not palindrome")
# print(type(list1))

# list = ["A" , "B" ,"C" , "A" ,"A" , "D", "F" , "A" , "F" , "A"]
# print(list.sort())
# print(list)
              
#traffic rules...
# age = 88
# if (age >= 18):
#     if (age <= 60):
#         print("you can drive")
#     elif(age >= 61 and age <= 80):
#         print("you can drive but in limited speed")
#     else:
#         print("you can not dive")
# else:
#     print("you cant drive") 


# DICTIONARY


# info = {
#     "name" : "Moh",
#     "father_name " : "Abdul ",
#     "subjects" : {
#         "phy" : 57,
#         "chem" : 55,
#         "math" : 65,
#     }
# }
# new_dic = {"surname" : "Bur","city" : "faisalabad"}
# info.update(new_dic)
# print(info)

#Sets in python 

# a = {1,2,3,4,5,6}
# b = {2 ,4,5,6, 7,8,9}
# union = a.intersection(b)
# print(union)
#3#################
# ############IMP......
# dic = {}
# x = int(input("enter physics marks : "))
# y = int(input("enter chemistry marks :"))
# z= int(input("Enter math marks :"))
# dic.update({"physics": x})
# dic.update({"chemistry": y})
# dic.update({"Math": z})
# print(tuple(dic))
     
     
#STORE SAME VALUE IN ONE SET  
#with crate tuples in set

# A = {
#     ("f", 2),
#     ("i", 2.0),
# }
# print(A)



# hours = float(input("Enter hours worked: "))
# rate = float(input("Enter rate per hour: "))

# # Calculate overtime hours and regular hours
# overtime_hours = max(hours - 40, 0)
# regular_hours = min(hours, 40)

# # Calculate gross pay
# gross_pay = (regular_hours * rate) + (overtime_hours * 1.5 * rate)

# # Print gross pay
# print("Gross pay: $", round(gross_pay, 2))



# for print list by loop 

# n  = [888,4,5,6,8,95,4,32,788,32532,4,5246,6]
# i = 3
# while i < len(n):
#     print(n[i])
#     i +=1  





# # #### FOR SEARCH A NUMBER IN TUPLE AND PRINT BY LOOP
# n = (2,3,5,6,7,8,9,0,33,44,9,666,9,99,)
# x = 9
# i = 0
# while i < len(n):
#     if(n[i] == x):
#         print("result" , i)
#         break
#     else :
#         print("finding ...")
#     i +=1
# print("end of loop")       
    
# i = 0 
# while i <= 10:
#     if (i % 2 == 1):
#         i +=1
#         continue    
#     print(i)
#     i +=1 
 
# tup = (1,2,4,6,9,25,34,54,67,87,98,100, 34)
# x = 34
# idx = 0
# for char in tup:
#     if(char == x):
#         print("index  : " ,idx)
#     idx +=1
# else : 
#     print("loop ending")
# seq = range(100)
# for i in seq :
#     print(i)
# n = int(input("enter step : "))
# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum +=i
#     i +=1
# print( "total sum =" , sum)
# n = 5
# fact = 1
# for i in range(1 , n+1 ):
#     fact *=i
# print("total fact  : " , fact)
    
# def sum (a,b):
#     sum = a + b
#     return sum
# n = sum(10, 20)
# print(n)
    
# def cal_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
# output = cal_avg(55,57,52)
# print(output) 


# n= [ "Ahsan" , "Mohsin", "Nasir" , "Ghafoor"  ]
# m = [ "quaid" , "iqbal" , " sayed" ,   " johar " , "sayed"  ]
# def print_len(list):
#     print(len(list))
# print_len(n)
# print_len(m)