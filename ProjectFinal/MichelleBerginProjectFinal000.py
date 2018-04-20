import turtle
from math import *
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)

def start(size):
    kokoro.pu()
    kokoro.back(size * 2)
    kokoro.lt(90)
    kokoro.fd(size / 2)
    kokoro.rt(90)
    kokoro.pd()
    
def diamond(side,h):
    kokoro.pu()
    kokoro.fd(side)
    kokoro.pd()
    kokoro.lt(60)
    for i in range(2):
        kokoro.fd(side)
        kokoro.rt(120)
        kokoro.fd(side)
        kokoro.rt(60)
    kokoro.rt(60)

def halfDiamond(side,h,d):
    kokoro.pu()
    kokoro.fd(side)
    kokoro.pd()
    kokoro.lt(60)
    kokoro.fd(side)
    kokoro.rt(150)
    kokoro.fd(h)
    kokoro.rt(150)
    kokoro.fd(side)
    kokoro.rt(150)

    
def hexagon(side,angle):
    kokoro.fd(side)
    kokoro.lt(angle)

def firstBox(h,side):
    kokoro.pu()
    kokoro.back(side)
    kokoro.pd()
    kokoro.lt(90)
    kokoro.fd(h)
    kokoro.begin_fill()
    kokoro.color('Slate Blue','Slate Blue')
    for i in range (3):
        kokoro.rt(90)
        kokoro.fd(200)
    kokoro.rt(90)
    kokoro.fd(200 - h)
    kokoro.rt(90)
    kokoro.end_fill()
    kokoro.pu()
    kokoro.fd(side / 2)
    kokoro.pd()

def hexagonRow(side,n,d,angle,h):
    for i in range (9):
        kokoro.begin_fill()
        if i % 2 == 0:
            kokoro.color('Midnight Blue','Medium Orchid')
            for d in range(n):
                hexagon(side,angle)
        else:
            kokoro.color('Midnight Blue','Steel Blue')
            for d in range(n):
                hexagon(side,angle)
        kokoro.end_fill()
        kokoro.begin_fill()
        if i % 2 == 0:
            kokoro.color('Midnight Blue','Plum')
            diamond(side,h)
        else:
            kokoro.color('Midnight Blue','Light Steel Blue')
            diamond(side,h)
        kokoro.end_fill()
        kokoro.pu()
        kokoro.fd(side)
        kokoro.pd()
    kokoro.begin_fill()
    if (i + 1) % 2 == 0:
        kokoro.color('Midnight Blue','Medium Orchid')
        for d in range(n):
            hexagon(side,angle)
    else:
        kokoro.color('Midnight Blue','Steel Blue')
        for d in range(n):
            hexagon(side,angle)
    kokoro.end_fill()
    kokoro.begin_fill()
    if (i + 1) % 2 == 0:
        kokoro.color('Midnight Blue','Plum')
        halfDiamond(side,h,d)
    else:
        kokoro.color('Midnight Blue','Light Steel Blue')
        halfDiamond(side,h,d)
    kokoro.end_fill()


def hexagonAll(size,n,angle):
    d = 20
    side = size / d
    h = sqrt(3) * side
    kokoro.pu()
    kokoro.rt(90)
    kokoro.fd(h / 2)
    kokoro.lt(90)
    kokoro.pd()
    firstBox(h,side)
    for i in range (9):
        hexagonRow(side,n,d,angle,h)
        kokoro.pu()
        kokoro.back(200)
        kokoro.pd()
    





##
##diamond(20)
start(200)
hexagonAll(200,6,60)
