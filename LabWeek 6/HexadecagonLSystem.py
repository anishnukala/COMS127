# hexadecagonLSystem.py
# Author: Anish Reddy Nukala
# Creation Date: 02-28-2024
# Lab 6
# Description: This script draws multiple hexadecagons in a line, with the ability to draw a single hexadecagon
# citation: https://en.wikipedia.org/wiki/Hexadecagon


import turtle
import random

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   
    elif ch == 'H':
        newstr = 'H'         
    elif ch == 'P':
        newstr = 'P'          
    else:
        newstr = ch    

    return newstr


def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'H':
            hexadecagonTurtle(aTurtle, distance)
        elif cmd == 'P':
            placeRandomly(aTurtle)

def hexadecagonTurtle(aTurtle, side_length):

    for _ in range(16):
        aTurtle.forward(side_length)
        aTurtle.left(360 / 16)

def placeRandomly(aTurtle):

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    aTurtle.penup()
    aTurtle.goto(x, y)
    aTurtle.pendown()

def main():
    inst = createLSystem(4, "F")   
    print(inst)
    t = turtle.Turtle()            
    wn = turtle.Screen()
    wn.bgcolor("yellow")

    t.up()
    t.color("red")
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 55)   
                                  
    wn.exitonclick()

if __name__ == "__main__":
    main()
