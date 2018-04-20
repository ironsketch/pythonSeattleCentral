# Importing turtle library
import turtle

# Importing specifically random integer from random library
from random import randint

# Importing all things from math
from math import *

# Declaring my window
wn = turtle.Screen()

# Setting my window BGcolor
wn.bgcolor('Dark Slate Gray')

# My title! It appears in the window top bar
wn.title('Go Home Turtle, You\'re DRUNK!')

# Assigning my turtle a name kokoro (variable)
kokoro = turtle.Turtle()

# Setting up my turtle color! which also sets line color
# which can also be changed too
kokoro.color('Medium Turquoise')
kokoro.speed(0)

# Setting up the main def for my drunk turtle
def drunkTurtle():

    # Setting up this variable to be used later
    d = 0

    # Setting up counter
    times = 1

    # Setting up list of colors
    colorList = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']

    # While statement, in the while statement we use the
    # squaring to get rid of - sign and then we compare
    # the result to see if it is greater than 200. If it
    # Is then we stop the turtle because the while
    # statement ends.
    while d <= 200:

        # Random int from 0 - 359
        randomNum = randint(0,359)
        color = randint(0,7)

        # Move kokoro forward 10
        kokoro.fd(10)

        # Pick up pen
        kokoro.pu()

        # Move forward 10
        kokoro.fd(10)

        # Put down pen
        kokoro.pd()

        # Left turn at random number
        kokoro.lt(randomNum)

        # Getting kokoro's position and simultaneously
        # assigning variables accordingly
        x,y = kokoro.pos()

        # Stopping Kokoro at radius d in the while loop
        d = sqrt(x**2 + y**2)

        # Counter to see how many times kokoro will move
        times += 1
        kokoro.pencolor(colorList[color])
        
    print (times)

# Calling main def
drunkTurtle()
