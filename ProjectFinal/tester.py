##     TEST     ##

import turtle
from math import *
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')
wn.screensize(1440, 900)
size = 200
d = 20
side = size / d
h = sqrt(3) * side
fart = h - side
def start(size):
    kokoro.pu()
    kokoro.back(size * 2)
    kokoro.lt(90)
    kokoro.fd(size / 2)
    kokoro.rt(90)
    kokoro.pd()
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
    kokoro.rt(60)
start(200)
halfDiamond(side,h,d)
