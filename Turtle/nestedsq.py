import turtle
from math import *
from random import randint


wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()

colorList = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']
kokoro.color('Medium Turquoise','Purple')
def randColor():
    color = randint(0,7)
    return color

def reposition():
    kokoro.pu()
    kokoro.bk(300)
    kokoro.rt(90)
    kokoro.fd(300)
    kokoro.lt(90)
    kokoro.pd()

def getReady(length,numberOfSquares):
    kokoro.lt(45)
    first = sqrt(length**2 + length**2)
    move = first / numberOfSquares
    kokoro.pu()
    kokoro.fd(move)
    kokoro.rt(45)
    kokoro.pd()

def squary(length,numberOfSquares):
    for i in range (numberOfSquares):
        kokoro.pencolor(colorList[randColor()])
        kokoro.color(colorList[randColor()],colorList[randColor()])
        kokoro.begin_fill()
        for i in range (4):
            kokoro.fd(length)
            kokoro.lt(90)
        kokoro.end_fill()
        getReady(length,numberOfSquares)
        length = (length / numberOfSquares) * (numberOfSquares - 2)

reposition()
squary(500,15)
kokoro.ht()
