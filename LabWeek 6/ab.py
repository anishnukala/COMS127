# TridecagonLSystem.py
#Anish Reddy Nukala
#09-25-2023
#Lab Week 6
# Description: This script draws multiple tridecagons in a line - one after the other.


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
        newstr = 'P-T++P-F'
    else:
        newstr=ch
            

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            drawTridecagon(aTurtle, distance)  
        elif cmd == 'P':
            placeRandomly(aTurtle)  

def drawTridecagon(aTurtle, side_length):

    for _ in range(13):
        aTurtle.forward(side_length)
        aTurtle.left(360 / 13)

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
