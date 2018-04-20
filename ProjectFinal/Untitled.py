import turtle
from math import *
from random import randint
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)

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
        kokoro.lt(90)

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

fillThefirstFractal(2, 90)
