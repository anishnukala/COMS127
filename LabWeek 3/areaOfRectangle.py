#areaOfRectangle.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates and prints the area of Rectangle.
#citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiqo4rvtZmEAxV3xuYEHYsJA3IQFnoECA8QAw&url=https%3A%2F%2Fwww.cuemath.com%2Fmeasurement%2Farea-of-rectangle%2F%23%3A~%3Atext%3DIt%2520is%2520calculated%2520using%2520the%2Cof%2520rectangle%2520%253D%2520length%2520%25C3%2597%2520width.&usg=AOvVaw3hskToC3wvvab4hyekNs9U&opi=89978449

import math

base= float(input("please enter the base of Rectangle:"))
height= float(input("please enter the height of Rectangle:"))

area = base * height

print(f"The area of Rectangle is {area} for base {base} and height {height}.")