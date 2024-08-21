#  - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable
celsius = float(input("enter temperature in celsius"))
fahrenheit = celsius * (9/5) + 32
print(fahrenheit)
fahrenheit = float(input("enter temperature in fahrenheit"))
celsius =   (fahrenheit - 32) * 5/9
print(celsius)
