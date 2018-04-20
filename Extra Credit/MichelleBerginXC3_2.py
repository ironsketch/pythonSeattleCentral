import turtle
from math import *
from random import randint


wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()

size = 45
a = sqrt((size**2) / 2)

def reposition():
    kokoro.pu()
    kokoro.bk(300)
    kokoro.lt(90)
    kokoro.fd(250)
    kokoro.rt(90)
    kokoro.pd()

def triangle(size,a):
    kokoro.lt(45)
    kokoro.fd(size)
    kokoro.rt(135)
    kokoro.fd(a)
    kokoro.rt(90)
    kokoro.fd(a)

def triangle_2(size,a):
    kokoro.lt(45)
    kokoro.fd(size)
    kokoro.lt(135)
    kokoro.fd(a)
    kokoro.lt(90)
    kokoro.fd(a)

def rectangle(size,a):
    for i in range (2):
        kokoro.fd(size)
        kokoro.lt(90)
        kokoro.fd(a)
        kokoro.lt(90)
    kokoro.fd(size)

def oneSide(size,a):
    triangle(size,a)
    kokoro.lt(90)
    rectangle(size,a)
    triangle_2(size,a)

def main(size,a):
    reposition()
    triangle(size,a)
    kokoro.lt(90)
    rectangle(size,a)
    triangle_2(size,a)
    
main(size,a)
