# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which rectangle
# has the greater area, or if the areas are the same.

length1 = float(input("What is the length of Rectangle 1: "))
width1 = float(input("What is the width of Rectangle 1: "))

length2 = float(input("What is the length of Rectangle 2: "))
width2 = float(input("What is the width of Rectangle 2: "))

rectangle1 = length1 * width1

rectangle2 = length2 * width2

print("Area of Rectangle 1:", format(rectangle1, ".2f"))

print("Area of Rectangle 2:", format(rectangle2, ".2f"))

if (rectangle1 == rectangle2):
    print("Areas Are The Same!")
elif (rectangle1 > rectangle2):
    print("Rectangle 1 Has The Greater Area!")
else:
    print("Rectangle 2 Has The Greater Area!")