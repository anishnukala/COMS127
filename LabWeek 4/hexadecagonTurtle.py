# hexadecagonTurtle.py
# Author: Anish Reddy Nukala
# Date: 02/07/2024
# Lab Number: 4
# Description: Draws a regular hexadecagon using the turtle
# Citation: Hexadecagon - Wikipedia = https://en.wikipedia.org/wiki/Hexadecagon

import turtle

def hexadecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize("15")
    t.color("red")
    screen = turtle.Screen()         
    screen.bgcolor("yellow")

    for _ in range(16):
        t.forward(s)
        t.left(23.5)  

if __name__ == "__main__":
    s = int(input("Enter the side length (s): "))
    x = int(input("Enter the x-coordinate of the first vertex: "))
    y = int(input("Enter the y-coordinate of the first vertex: "))

    my_turtle = turtle.Turtle()
    my_turtle.speed("slow")  

    hexadecagonTurtle(s, x, y, my_turtle)

    turtle.done()



