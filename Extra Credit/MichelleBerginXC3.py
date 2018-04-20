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

def octagon(size):
    for i in range(8):
        kokoro.fd(size)
        kokoro.rt(45)
        
def setUp(a):
    kokoro.pu()
    kokoro.rt(90)
    kokoro.fd(a)
    kokoro.lt(90)
    kokoro.back(a)
    kokoro.pd()

def turn(a):
    kokoro.fd(a)
    kokoro.lt(90)
    kokoro.fd(a)
    kokoro.back(a)
    kokoro.rt(90)
    
def inside(size,a):
    kokoro.fillcolor(128,128,128)
    for i in range(4):
        kokoro.begin_fill()
        kokoro.fd(a)
        kokoro.lt(90)
        kokoro.fd(a)
        kokoro.back(a)
        kokoro.rt(90)
        kokoro.end_fill()
        kokoro.fd(size)
        kokoro.lt(90)
        kokoro.fd(a)
        kokoro.back(a)
        kokoro.rt(90)
        kokoro.fd(a)
        kokoro.back(a)
        kokoro.rt(90)
        

def main(size,a):
    reposition()
    octagon(size)
    setUp(a)
    inside(size,a)
    
main(size,a)
