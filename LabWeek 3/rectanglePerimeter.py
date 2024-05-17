#rectanglePerimeter.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates and prints the perimeter of Rectangle.
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjUi7jZtpmEAxXMwOYEHYwlAYwQFnoECBUQAw&url=https%3A%2F%2Fwww.mometrix.com%2Facademy%2Fcalculating-the-perimeter-of-rectangles%2F%23%3A~%3Atext%3DThe%2520perimeter%2520formula%2520for%2520a%2Cto%2520solve%2520for%2520the%2520perimeter.&usg=AOvVaw0d1n2czJrDl84Qy3bT9RyS&opi=89978449

import math

length= float(input("please enter the length of Rectangle:"))
width= float(input("please enter the width of Rectangle:"))

perimeter = 2 * (length + width)

print(f"The perimeter of Rectangle is {perimeter} for length {length} and width {width}.")