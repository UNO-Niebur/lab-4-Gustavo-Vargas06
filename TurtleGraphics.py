#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    myTurtle.penup()
    myTurtle.goto(-50, 100)
    myTurtle.pendown()
    def drawpoly(myTurtle, sides):
        angle = 360 / sides
        for i in range(sides):
            myTurtle.forward(50)
            myTurtle.right(angle)
    # drawPolygon(myTurtle, 5) #draws a pentagon
    drawpoly(myTurtle, 5)
    # drawPolygon(myTurtle, 8) #draws an octogon
    drawpoly(myTurtle, 8)
    

    myTurtle = turtle.Turtle()
    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()
    def fillcorner(myTurtle, corner):
        for i in range(4):
            myTurtle.forward(200)
            myTurtle.right(90)
        if corner == 1:
            myTurtle.begin_fill()
            for i in range(4):
                myTurtle.forward(100)
                myTurtle.right(90)
            myTurtle.end_fill()
        elif corner == 2:
            myTurtle.goto(0, 100)
            myTurtle.begin_fill()
            for i in range(4):
                myTurtle.forward(100)
                myTurtle.right(90)
            myTurtle.end_fill()
        elif corner == 3:
            myTurtle.goto(-100, 0)
            myTurtle.begin_fill()
            for i in range(4):
                myTurtle.forward(100)
                myTurtle.right(90)
            myTurtle.end_fill()
        elif corner == 4:
            myTurtle.penup()
            myTurtle.goto(0, 0)
            myTurtle.pendown()
            myTurtle.begin_fill()
            for i in range(4):
                myTurtle.forward(100)
                myTurtle.right(90)
                myTurtle.end_fill()
            
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    fillCorner(myTurtle, 2)
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    fillCorner(myTurtle, 3)
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
