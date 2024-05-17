#circleCircumference.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates and prints the circumference of circle
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjl6aettpmEAxUoMjQIHXkhBJEQFnoECC0QAQ&url=https%3A%2F%2Fwww.omnicalculator.com%2Fmath%2Fcircumference&usg=AOvVaw0lyoC9VpKRNex1RyWkWXQm&opi=89978449
import math

radius= float(input("please enter the radius of the circle:"))

circumference= 2 * math.pi + radius

print(f"The circumference of circle is {circumference} for the radius {radius}.")