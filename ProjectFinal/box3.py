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

def boxSetUp(boxLength,color):
    kokoro.begin_fill()
    kokoro.color(color)
    for i in range(4):
        kokoro.fd(boxLength)
        kokoro.rt(90)
    kokoro.end_fill()

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
    kokoro.color('White','White')
    if order == 0:
        for i in range (3):
            kokoro.left(120)
            kokoro.fd(size)
    else:
        for i in range (3):
            sierpinski(order - 1, size / 2)
            kokoro.pu()
            kokoro.left(120)
            kokoro.fd(size)
            kokoro.pd()
            
def setUpSier(order,size):
    sierLines()
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(4)
    kokoro.pd()
    kokoro.begin_fill()
    kokoro.color('White','Black')
    sierLarge()
    kokoro.end_fill()
    kokoro.pu()
    kokoro.rt(180)
    kokoro.pd()
    sierpinski(order, size)
boxSetUp(200,'Black')
setUpSier(4,200)
