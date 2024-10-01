#trafic rules...
age = 88
if (age >= 18):
    if (age <= 60):
        print("you can drive")
    elif(age >= 61 and age <= 80):
        print("you can drive but in limited speed")
    else:
        print("you can not dive")
else:
    print("you cant drive") 