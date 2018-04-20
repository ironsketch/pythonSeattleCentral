import turtle
from math import *
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)


def start(boxLength):
    kokoro.pu()
    kokoro.back(boxLength * 2)
    kokoro.lt(90)
    kokoro.fd(boxLength / 2)
    kokoro.rt(90)
    kokoro.pd()

def boxSetUp(boxLength):
    for i in range(4):
        kokoro.fd(boxLength)
        kokoro.rt(90)

def circle():
    radius = 80
    counter = 1
    kokoro.fd(100)
    kokoro.lt(180)
    for i in range (1,15):
        
        kokoro.circle(radius,180)
        kokoro.rt(90)
        radius /= counter
        counter += .1

boxSetUp(200)
circle()
