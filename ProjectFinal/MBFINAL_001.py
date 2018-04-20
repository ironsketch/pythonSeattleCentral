import turtle
from math import *
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Midnight Blue')
wn.screensize(1440, 900)

def start(width):
    kokoro.pu()
    kokoro.back(size * 2)
    kokoro.lt(90)
    kokoro.fd(size / 2)
    kokoro.rt(90)
    kokoro.pd()

def rightTriangle(side,h,oneThird):
    kokoro.fd(h / 2)
    kokoro.rt(90)
    kokoro.fd(oneThird)
    kokoro.rt(120)
    kokoro.fd(side)

def fourRightTriangles(side,h,oneThird):
    kokoro.lt(90)
    rightTriangle(side,h,oneThird)
    kokoro.lt(30)
    rightTriangle(side,h,oneThird)

def hexagon(side):
    for i in range (6):
        kokoro.fd(side)
        kokoro.lt(60)

def main(n,d):
    boxLength = d * 10
    side = d / 2 # side is the length of one side 
    h = sqrt(3) * side # h stands for height
    oneThird = (d - side) / 2 # one small side of the width
    
    fourRightTriangles(side,h,oneThird)
    
main(6,200)
