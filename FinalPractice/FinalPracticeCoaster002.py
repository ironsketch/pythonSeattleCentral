import turtle
from math import *
from random import randint
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
kokoro.speed(0)

def hexagon(sz):
    for i in range (6):
        kokoro.fd(sz / 2)
        kokoro.rt(60)

def hexFromCenter(sz,lineClr,fillClr,lineSz):
    kokoro.pu()
    kokoro.lt(45)
    kokoro.fd(sz / 2)
    kokoro.pd()

    # Hex
    kokoro.begin_fill()
    kokoro.color(lineClr,fillClr)
    kokoro.pensize(lineSz)
    hexagon(sz)
    kokoro.end_fill()
    # End hex
    
    kokoro.pu()
    kokoro.rt(60)
    kokoro.fd(sz / 2)
    kokoro.lt(60)

def hexInHexFromCenter(sz,lineClr,fillClr,lineSz):
    h = sqrt(3) * (sz / 2)
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(h / 2)
    kokoro.rt(120)
    kokoro.pd()
    
    # Hex
    kokoro.begin_fill()
    kokoro.color(lineClr,fillClr)
    kokoro.pensize(lineSz)
    hexagon(h)
    kokoro.end_fill()
    # End hex

    kokoro.pu()
    kokoro.rt(60)
    kokoro.fd(h / 2)
    kokoro.pd()

def allHexs(sz,ln):
    kokoro.pu()
    kokoro.rt(45)
    kokoro.back(sz)
    kokoro.pd()
    hexFromCenter(sz,'Medium Turquoise','Cadet Blue',ln)
    hexInHexFromCenter(sz,'Lavender','Thistle',ln)
    h = sqrt(3) * (sz / 2)
    kokoro.pu()
    kokoro.rt(120)
    kokoro.back(h)
    kokoro.lt(60)
    kokoro.pd()
    
    for i in range (6):
        kokoro.pu()
        kokoro.rt(15)
        kokoro.pd()
        hexFromCenter(sz,'Medium Turquoise','Cadet Blue',ln)
        hexInHexFromCenter(sz,'Lavender','Thistle',ln)
    
        

allHexs(150,2)
