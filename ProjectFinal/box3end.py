import turtle
from math import *
from random import randint
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)

def triangleLeft(sz):
    kokoro.begin_fill()
    kokoro.color('White','Light Pink')
    for i in range (3):
        kokoro.fd(sz)
        kokoro.lt(120)
    kokoro.end_fill()

def triangleRight(sz):
    kokoro.begin_fill()
    kokoro.color('White','Sky Blue')
    for i in range (3):
        kokoro.fd(sz)
        kokoro.rt(120)
    kokoro.end_fill()
        
def manyTriangles(sz):
    for i in range (2):
        triangleLeft(sz)
        triangleRight(sz)
        kokoro.lt(60)
        kokoro.fd(sz)
        kokoro.rt(60)
    triangleRight(sz)
    kokoro.rt(60)
    kokoro.fd(sz)
    kokoro.lt(60)
    triangleLeft(sz)

def finalBit(sz):
    kokoro.pu()
    kokoro.fd(sz)
    kokoro.pd()
    triangleLeft(sz)
    triangleRight(sz)
    kokoro.fd(sz)
    kokoro.lt(60)
    triangleLeft(sz)
    kokoro.lt(60)
    kokoro.fd(sz)
    kokoro.rt(60)
    triangleRight(sz)
    kokoro.rt(60)
    kokoro.fd(sz)
    kokoro.rt(120)
    kokoro.begin_fill()
    kokoro.color('White','Sky Blue')
    kokoro.fd(sz * 2)
    kokoro.lt(120)
    kokoro.fd(sz)
    for i in range (2):
        kokoro.lt(60)
        kokoro.fd(sz)
    kokoro.end_fill()
    
def lastHexRow(sz):
    for i in range (4):
        for i in range (2):
            manyTriangles(sz)
            kokoro.fd(sz)
            kokoro.lt(60)
            kokoro.pu()
            kokoro.fd(sz)
            kokoro.pd()
            kokoro.rt(60)
            kokoro.rt(120)
        finalBit(sz)
        kokoro.lt(120)
        kokoro.pu()
        kokoro.fd(sz * 3)
        kokoro.pd()
        
lastHexRow(10)
