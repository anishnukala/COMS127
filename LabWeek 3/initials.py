# initials.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: prints my initials Anish Nukala (AN)

import turtle

screen = turtle.Screen()         
screen.bgcolor("yellow")

anish_turtle = turtle.Turtle()
anish_turtle.speed(1)  

anish_turtle.color("blue")
anish_turtle.penup()
anish_turtle.pensize(5)
anish_turtle.goto(-50, 0)
anish_turtle.pendown()
anish_turtle.left(75)
anish_turtle.forward(100)
anish_turtle.right(150)
anish_turtle.forward(100)
anish_turtle.backward(40)
anish_turtle.right(75)
anish_turtle.forward(40)


nukala_turtle = turtle.Turtle()
nukala_turtle.speed(1)

nukala_turtle.color("red")
nukala_turtle.penup()
nukala_turtle.pensize(5)
nukala_turtle.goto(100, 0)
nukala_turtle.pendown()
nukala_turtle.left(90)
nukala_turtle.forward(100)
nukala_turtle.right(135)
nukala_turtle.forward(140)
nukala_turtle.left(135)
nukala_turtle.forward(100)

turtle.done()
screen.exitonclick()
