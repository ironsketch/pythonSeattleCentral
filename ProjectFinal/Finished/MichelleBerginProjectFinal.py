## YOUTUBE ADDY: https://youtu.be/YwUmysMd_kc

import turtle
from math import *
from random import randint
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)
kokoro.speed(0)

colorList = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']

# I use this for random colors
def randColor():
    color = randint(0,7)
    return color

# This is to set up the turtle at the very beginning
def start(boxLength):
    kokoro.pu()
    kokoro.back(boxLength * 2)
    kokoro.lt(90)
    kokoro.fd(boxLength / 2)
    kokoro.rt(90)
    kokoro.pd()

# This is to set up each initial box
def boxSetUp(boxLength,color):
    kokoro.begin_fill()
    kokoro.color(color)
    for i in range(4):
        kokoro.fd(boxLength)
        kokoro.rt(90)
    kokoro.end_fill()

## SIMPLE FIRST BOX ###########################

def triangleinBox(side):

    # Creating the triangles on top of the box just created
    kokoro.begin_fill()
    kokoro.color(colorList[randColor()],colorList[randColor()])
    diagonal = side * sqrt(2)
    kokoro.rt(45)
    kokoro.fd(diagonal)
    kokoro.lt(135)
    kokoro.fd(side)
    kokoro.lt(135)
    kokoro.fd(diagonal)
    kokoro.rt(135)
    kokoro.fd(side)
    kokoro.rt(90)
    kokoro.end_fill()
    
    
def box(boxLength,n,side):
    kokoro.begin_fill()
    kokoro.color(colorList[randColor()],colorList[randColor()])

    # Making the box
    for i in range(4):
        kokoro.fd(side)
        kokoro.rt(90)
    kokoro.end_fill()

    # Creating the triangles on top
    triangleinBox(side)

def rowOfBoxes(boxLength,n,side,iteration):
    for i in range(n):

        # Create the box
        box(boxLength,n,side)
        kokoro.pu()

        # Move forward for next box
        kokoro.fd(side)
        kokoro.pd()

def allBoxes(boxLength,n):

    # I divide the box length with the number of
    # boxes I want to run accross
    side = boxLength / n
    for i in range(n):

        # Run rowOfBoxes
        rowOfBoxes(boxLength,n,side,i)
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(side)
        kokoro.lt(90)

        # Go back to do the next row
        kokoro.back(boxLength)
        kokoro.pd()

## END SIMPLE FIRST BOX #########################

## SIMPLE HEXAGON ###############################
def fullHex(side):

    # Each Hexagon
    for i in range(6):
        kokoro.fd(side)
        kokoro.rt(60)
        
def rowHex(side,h,d,it):
    short = d / 4
    kokoro.pu()
    kokoro.fd(short)
    kokoro.pd()

    # If the iteration that was passed through
    # Divided by 2 == 0 then run this
    if it % 2 == 0:
        for i in range (6):
            kokoro.begin_fill()
            kokoro.color('White','Light Salmon')
            
            # First HEX
            fullHex(side)
            kokoro.end_fill()
            kokoro.pu()
            kokoro.rt(30)
            kokoro.fd(h)
            kokoro.lt(30)
            kokoro.pd()
            kokoro.begin_fill()
            kokoro.color('White','Wheat')
            
            # Second HEX
            fullHex(side)
            kokoro.end_fill()
            kokoro.pu()
            kokoro.lt(30)
            kokoro.fd(h)
            kokoro.pd()
            kokoro.rt(30)
        kokoro.begin_fill()
        kokoro.color('White','Light Salmon')
        
        # 13th HEX
        fullHex(side)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.rt(30)
        kokoro.fd(h)
        kokoro.lt(30)
        kokoro.pd()

    # else if anything else run this
    else:
        for i in range (6):
            kokoro.begin_fill()
            kokoro.color('White','Tomato')
            # First HEX
            fullHex(side)
            kokoro.end_fill()
            kokoro.pu()
            kokoro.rt(30)
            kokoro.fd(h)
            kokoro.lt(30)
            kokoro.pd()
            kokoro.begin_fill()
            kokoro.color('White','Orange')
            
            # Second HEX
            fullHex(side)
            kokoro.end_fill()
            kokoro.pu()
            kokoro.lt(30)
            kokoro.fd(h)
            kokoro.pd()
            kokoro.rt(30)
        kokoro.begin_fill()
        kokoro.color('White','Tomato')
        
        # 13th HEX
        fullHex(side)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.rt(30)
        kokoro.fd(h)
        kokoro.lt(30)
        kokoro.pd()

def allHex(side):
    h = sqrt(3) * side
    d = 20

    # Creating each row
    for i in range (11):

        # Each row
        rowHex(side,h,d,i)
        kokoro.pu()

        # Heading back to start next row
        kokoro.back(200)
        kokoro.rt(90)
        kokoro.fd(h / 2)
        kokoro.lt(90)
        kokoro.pd()

## END SIMPLE HEXAGON ###############################

## Begin Complex 3rd Box ############################

def triangleLeft(sz):
    kokoro.begin_fill()
    kokoro.color('White','Light Pink')

    # Creating the Triangle
    for i in range (3):
        kokoro.fd(sz)
        kokoro.lt(120)
    kokoro.end_fill()

def triangleRight(sz):
    kokoro.begin_fill()
    kokoro.color('White','Sky Blue')

    # Creating the Triangle
    for i in range (3):
        kokoro.fd(sz)
        kokoro.rt(120)
    kokoro.end_fill()

def manyTriangles(sz):

    # Because the triangles alternate I made 2 helper def
    for i in range (2):

        # Triangle turning left
        triangleLeft(sz)

        # Triangle turning right
        triangleRight(sz)
        kokoro.lt(60)
        kokoro.fd(sz)
        kokoro.rt(60)

    # Here's the odd triangles!
    triangleRight(sz)
    kokoro.rt(60)
    kokoro.fd(sz)
    kokoro.lt(60)
    triangleLeft(sz)

def manyManyTriangles(sz):

    # This creates the triangles plus the odd triangle out
    for i in range (3):

        # This calls the row of triangles
        manyTriangles(sz)
        kokoro.fd(sz)
        kokoro.lt(60)
        kokoro.fd(sz)
        kokoro.rt(60)
        kokoro.rt(120)

def hexed(sz):
    for i in range (5):

        # I start by creating the triangles around the hexagon
        manyManyTriangles(sz)
        kokoro.fd(sz)
        kokoro.lt(60)
        kokoro.begin_fill()
        kokoro.color('White','White')

        # Then I had the turtle make the hexagon inside
        for i in range (6):
            kokoro.fd(sz)
            kokoro.rt(60)
        kokoro.end_fill()
        kokoro.rt(60)
        kokoro.pu()

        # Forward to make the next hexagon
        kokoro.fd(sz * 3)
        kokoro.pd()

def finalBit(sz):

    # This mess handles the mess at the end of the odd drawings
    kokoro.pu()
    kokoro.fd(sz)
    kokoro.pd()
    triangleLeft(sz)
    triangleRight(sz)
    kokoro.fd(sz)
    kokoro.lt(60)
    triangleLeft(sz)
    kokoro.lt(60)
    kokoro.fd(sz)
    kokoro.rt(60)
    triangleRight(sz)
    kokoro.rt(60)
    kokoro.fd(sz)
    kokoro.rt(120)
    kokoro.begin_fill()
    kokoro.color('White','White')
    kokoro.fd(sz * 2)
    kokoro.lt(120)
    kokoro.fd(sz)
    for i in range (2):
        kokoro.lt(60)
        kokoro.fd(sz)
    kokoro.end_fill()

def lastHexRow(sz):

    # We will make 5 partial drawings
    for i in range (5):

        # They only need 2 triangle repititions since the last one is odd
        for i in range (2):
            manyTriangles(sz)
            kokoro.fd(sz)
            kokoro.lt(60)
            kokoro.pu()
            kokoro.fd(sz)
            kokoro.pd()
            kokoro.rt(60)
            kokoro.rt(120)

        # The odd part is handled by finalBits
        finalBit(sz)
        kokoro.lt(120)
        kokoro.pu()
        kokoro.fd(sz * 3)
        kokoro.pd()

def hexes(boxLength):
    boxSetUp(boxLength,'Grey')
    kokoro.color('White','Tomato')
    kokoro.rt(90)
    kokoro.pu()
    kokoro.fd(17)
    kokoro.pd()
    kokoro.lt(90)

    # Creating all rows of the Hexagons
    for i in range(5):

        # Creating each row
        hexed(10)
        kokoro.pu()

        # Gowing back to start new row
        kokoro.back(boxLength)
        kokoro.rt(90)
        kokoro.fd(35)
        kokoro.lt(90)
        kokoro.pd()

    # Then I have the last row which is an odd ball
    lastHexRow(10)

## End Complex 3rd Box ##############################

## Begin Complex 4th Box ############################
## 12 Sided polygon      ############################

def squarePoly12(sz):

    # Only 3 sides of the square because:
    for i in range (3):
        kokoro.lt(90)
        kokoro.fd(sz)
    kokoro.lt(90)

    # The last side I didn't want to draw
    # I wanted the shapes to look funny and somewhat like a gear
    kokoro.pu()
    kokoro.fd(sz)
    kokoro.pd()

def polygonPoly12 (sz):

    # The dodecahedron is a 12 sided shape
    # So I have this running half that since I accomplish
    # Two sides every itteration
    for i in range (6):
        kokoro.pu()

        # One side
        kokoro.fd(sz)
        kokoro.pd()

        # Second side that is a square
        squarePoly12(sz)
        kokoro.rt(30)
        kokoro.fd(sz)
        kokoro.rt(30)

def rowPoly12 (sz,num):

    # A specific list to create the rainbow effect
    colorList = ['Blue','Hot Pink','Dark Orange','Spring Green',
                 'Purple','Red','Yellow','Dark Turquoise']
    kokoro.pu()
    kokoro.fd(7 + sz)
    kokoro.rt(90)
    kokoro.fd(sz)
    kokoro.lt(90)
    kokoro.pd()

    # Creating a row of my shapes
    for i in range (4):
        kokoro.begin_fill()
        kokoro.color(colorList[num + i],'gray12')

        # Drawing each shape
        polygonPoly12 (sz)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.fd(45)
        kokoro.pd()

def alterRowPoly12(sz):

    # This is creating all the rows
    for i in range (7):

        # This is creating each other row
        rowPoly12(sz,0)
        kokoro.pu()

        # Heading back to create the next row
        kokoro.back(195)
        kokoro.rt(90)
        kokoro.fd(sz + 2)
        kokoro.lt(90)
        kokoro.fd(sz * 4 + 4)
        kokoro.pd()

        # This is the next row
        rowPoly12(sz,4)
        kokoro.pu()

        # Heading back to do it all over again
        kokoro.back(215)
        kokoro.rt(90)
        kokoro.fd(sz + 2)
        kokoro.lt(90)
        kokoro.pd()

## End Complex 4th Box ##############################

## Begin First Simple Fractal #######################
def firstFractal(order, size):

    # The order starts at 2
    if order == 0:
        kokoro.forward(size)
    else:

        # It will go here and remember that it was called but it will -1
        # From it's order and it will go back to the if/else statement
        # From there it will repeat until it can accomplish something
        # All the while remembering how many times it was called.
        # Finally when order == 0 it will accomplish the if
        # BUT it still has all the stored info in regards to calling itself
        # RECURSION
        firstFractal(order - 1, size / 3)

        # Now it can finally accomplish this turn
        kokoro.right(85)

        # And this back and forth of getting to order 0 and storing
        # the idea that it needs to do each of these again continues
        # Until it no longer calls it's self
        firstFractal(order - 1, size / 3)
        kokoro.left(170)
        firstFractal(order - 1, size / 3)
        kokoro.right(85)
        firstFractal(order - 1, size / 3)

def manyfirstFractal(order,size):

    # We do this 4 times for each fractal
    # Turning each time to make a full design
    for i in range(4):
        firstFractal(order,size)
        kokoro.rt(90)

def rowOffirstFractal(order,size):

    # This is creating each row. We run it twice to create a row of 4
    for i in range (2):
        kokoro.begin_fill()
        kokoro.color('Dark Turquoise','Sky Blue')

        # Creating the full fractal
        manyfirstFractal(order, size)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.forward(50)
        kokoro.pd()
        kokoro.begin_fill()
        kokoro.color('Dark Turquoise','White')

        # Creating the full fractal
        manyfirstFractal(order, size)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.forward(50)
        kokoro.pd()

def fillThefirstFractal(order,size):
    kokoro.pu()
    kokoro.fd(1)
    kokoro.rt(90)
    kokoro.fd(1)
    kokoro.lt(90)
    kokoro.pd()

    # This sets up all the rows
    for i in range (4):

        # This is each row
        rowOffirstFractal(order,size)
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(50)
        kokoro.lt(90)

        # Heading back to set up for the next row
        kokoro.back(200)
        kokoro.pd()
        
## END First Simple Fractal #########################

## Begin Sierpinski Fractal #########################

def sierLines():
    kokoro.rt(90)
    for i in range (25):
        colorCounter = 0
        for i in range (8):
            kokoro.pencolor(colorList[colorCounter])
            kokoro.fd(25)
            colorCounter += 1
        kokoro.pu()
        kokoro.lt(90)
        kokoro.fd(4)
        kokoro.lt(90)
        kokoro.pd()
        colorCounter = 7
        for i in range (8):
            kokoro.pencolor(colorList[colorCounter])
            kokoro.fd(25)
            colorCounter -= 1
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(4)
        kokoro.rt(90)
        kokoro.pd()
    colorCounter = 0
    for i in range (8):
        kokoro.pencolor(colorList[colorCounter])
        kokoro.fd(25)
        colorCounter += 1
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(4)
    kokoro.lt(90)
    kokoro.pd()

def sierLarge():
    for i in range (3):
        kokoro.fd(200)
        kokoro.rt(120)
        
def sierpinski(order, size):

    # I chose only white and not filling it
    kokoro.color('White','White')

    # Again the order will be 0 to make a triangle
    if order == 0:
        for i in range (3):
            kokoro.left(120)
            kokoro.fd(size)
    else:

        # Stored, everytime it calls it's self it does it 3 times
        # That's why the triangles repeat three times every time
        for i in range (3):
            sierpinski(order - 1, size / 2)
            kokoro.pu()
            kokoro.left(120)
            kokoro.fd(size)
            kokoro.pd()
            
def setUpSier(order,size):

    # This is setting up pretty rainbow vertical lines
    sierLines()
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(4)
    kokoro.pd()
    kokoro.begin_fill()
    kokoro.color('White','Black')

    # This is setting up one BIG triangle
    sierLarge()
    kokoro.end_fill()
    kokoro.pu()
    kokoro.rt(180)
    kokoro.pd()

    # This is the recurrsion called a Sierpinski triangle
    sierpinski(order, size)

## End Sierpinski Fractal #########################

def main(boxLength):
    start(boxLength)
    boxSetUp(boxLength,'Black') # First BOX
    allBoxes(boxLength,10) # First Design
    kokoro.pu()
    kokoro.fd(boxLength)
    kokoro.lt(90)
    kokoro.fd(boxLength)
    kokoro.rt(90)
    kokoro.pd()
    boxSetUp(boxLength,'White') # Second BOX
    allHex(10) # Second Design
    kokoro.pu()
    kokoro.rt(90)
    kokoro.fd((sqrt(3) * 10) / 2)
    kokoro.lt(90)
    kokoro.pd()
    kokoro.fd(boxLength)
    kokoro.lt(90)
    kokoro.fd(boxLength - 1)
    kokoro.rt(90)
    boxSetUp(boxLength,'Grey') # Third BOX
    hexes(200) # Third Design
    kokoro.pu()
    kokoro.rt(90)
    kokoro.fd(8)
    kokoro.lt(180)
    kokoro.fd(boxLength)
    kokoro.rt(90)
    boxSetUp(boxLength,'Black') # Fourth BOX
    alterRowPoly12(5.35898) # Fourth Design
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(180)
    kokoro.rt(90)
    kokoro.back(201)
    kokoro.lt(90)
    kokoro.fd(198)
    kokoro.rt(90)
    boxSetUp(boxLength,'Thistle') # Fifth BOX
    fillThefirstFractal(2, 90) # Fifth Design
    kokoro.pu()
    kokoro.rt(90)
    kokoro.fd(200)
    kokoro.lt(90)
    kokoro.back(1)
    kokoro.pd()
    boxSetUp(boxLength,'Black') # Sixth BOX
    setUpSier(4,200) # Sixth Design!
    kokoro.hideturtle()
    

main(200)

## YOUTUBE ADDY: https://youtu.be/YwUmysMd_kc
