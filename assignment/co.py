def calculate_cylinder_volume(radius, height):
    pie_value = 3.1416
    volume = pie_value * (radius ** 2) * height
    print("Volume of Cylinder is:", volume)

print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))

calculate_cylinder_volume(radius, height)