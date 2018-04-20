import turtle
from math import *
from random import randint

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(128,128,128)
wn.title('Kokoro Circles')
kokoro = turtle.Turtle()

def ranColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

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
    
def fourCrclsInACrcl(Rad):
    circleCntr(Rad)
    r = Rad/(1 + sqrt(2))
    kokoro.pu()
    kokoro.lt(45)
    d = r + r*(sqrt(2) - 1)
    kokoro.fd(d)
    kokoro.rt(45)
    kokoro.pd()
    for i in range (4):
        CircleClr(r,2,ranColor(),ranColor())
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(r * 2)
        kokoro.pd()
    
fourCrclsInACrcl(200)
