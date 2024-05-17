# myShapes.py
#Anish Reddy Nukala
#09-25-2024
#Lab 5
# Description: It allows the user to choose shapes and answer to user 

import math
print("Choose an option:")
print("1. Calculate area of rectangle")
print("2. Calculate perimeter of rectangle")
print("3. Calculate area of circle")
print("4. Calculate circle of circumference")
choice= input("Enter your choice (1/2/3/4): ")


def areaOfRectangle(base,height):
    area = (base * height)
    return area

def rectanglePerimeter(length,width):
    perimeter = 2 * (length + width)
    return perimeter

def areaOfCircle(radius):
    area = math.pi * (radius ** 2)
    return area

def circleCircumference(radius):
    circumference= 2 * math.pi + radius
    return circumference
    
if choice == '1':
        base= float(input("please enter the base of Rectangle:"))
        height= float(input("please enter the height of Rectangle:"))
        area = areaOfRectangle(base,height)
        print(f"The area of Rectangle is {area} for base {base} and height {height}.")

elif choice == '2':
  length= float(input("please enter the length of Rectangle:"))
  width= float(input("please enter the width of Rectangle:"))
  perimeter = rectanglePerimeter(length,width)
  print(f"The perimeter of Rectangle is {perimeter} for length {length} and width {width}.")

elif choice == '3':
  radius= float(input("please enter the radius of the circle:"))
  area = areaOfCircle(radius)
  print(f"The area of circle is {area} for the radius {radius}.")

elif choice == '4':
        radius= float(input("please enter the radius of the circle:"))
        circumference = circleCircumference(radius)
        print(f"The circumference of circle is {circumference} for the radius {radius}.")
else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")