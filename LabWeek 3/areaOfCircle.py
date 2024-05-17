#areaOfCircle.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Clculates and prints the area of circle
# Citation:# Citation: https://www.wikihow.com/Calculate-the-Area-of-a-Circle

import math

radius= float(input("please enter the radius of the circle:"))

area = math.pi * (radius ** 2)

print(f"The area of circle is {area} for the radius {radius}.")