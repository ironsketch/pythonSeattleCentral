import turtle
from math import *
from random import randint

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(128,128,128)
wn.title('Kokoro Circles')
kokoro = turtle.Turtle()
Rad = 200
r = Rad/(1 + sqrt(2))
lineColor = 220,220,220
fillColor = 169,169,169

def center2edge(Rad):
    kokoro.pu()
    kokoro.fd(Rad)
    kokoro.lt(90)
    kokoro.pd()
    
def edge2center(Rad):
    kokoro.pu()
    kokoro.rt(90)
    kokoro.back(Rad)
    kokoro.pd()

def circleCntr(Rad):
    center2edge(Rad)
    kokoro.circle(Rad)
    edge2center(Rad)

def CircleClr(Rad,lineSize,lineColor,fillColor):
    kokoro.pencolor(lineColor)
    kokoro.pensize(lineSize)
    kokoro.fillcolor(fillColor)
    kokoro.begin_fill()
    circleCntr(Rad)
    kokoro.end_fill()

CircleClr(r,2,lineColor,fillColor)
