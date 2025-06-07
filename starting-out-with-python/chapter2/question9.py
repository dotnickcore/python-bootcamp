import math

radius = float(input("Enter the radius: "))

radius_of_circle = math.pi*(radius**2)
circumference_of_circle = 2*math.pi*radius

print("Radius of the Circle:", format(radius_of_circle, '.2f'))
print("Circumference of the Circle:", format(circumference_of_circle, '.2f'))