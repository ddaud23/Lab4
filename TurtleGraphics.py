#TurtleGraphics.py
#Name:Daud Daud
#Date:
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(MOE, sides):
    for s in range(sides):
        MOE. forward(50)
        MOE. left(360/sides)
        
def fillCorner(MOE, corner):
    # Draw big square
    drawSquare(MOE, 75)
    
    if corner == 1:  
        MOE.begin_fill()
        drawSquare(MOE, 50)
        MOE.end_fill()

    elif corner == 2:  
        MOE.forward(25)  
        MOE.begin_fill()
        drawSquare(MOE, 50)
        MOE.end_fill()

    elif corner == 3: 
        MOE.right(90) 
        MOE.forward(25)  
        MOE.left(90)  
        MOE.begin_fill()
        drawSquare(MOE, 50)
        MOE.end_fill()

    elif corner == 4:  
        MOE.forward(50)  
        MOE.right(90)  
        MOE.forward(25) 
        MOE.left(90)  
        MOE.begin_fill()
        drawSquare(MOE, 50)
        MOE.end_fill()


def draw_square(myTurtle, size):
    """Draws a square of given size."""
    myTurtle.penup()
    myTurtle.goto(-size / 2, size / 2)  
    myTurtle.pendown()
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def squaresInSquares(myTurtle, n):
    """Draws n concentric squares, each fitting inside the next."""
    size = n * 20 
    for _ in range(n):
        draw_square(myTurtle, size)
        size -= 20  
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 75)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 12)

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    #fillCorner(myTurtle, 4) #draws a square with bottom right corner filled in.
    #fillCorner(myTurtle, 1) #draws a square with top left corner filled in.
    
    
    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares

main()
