from math import *
import turtle

wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.speed(0)
kokoro.pensize(2)

def start():
    kokoro.pu()
    kokoro.bk(240)
    kokoro.lt(90)
    kokoro.fd(200)
    kokoro.rt(90)
    kokoro.pd()

def triangle(sz):
    for i in range (3):
        kokoro.fd(sz)
        kokoro.lt(120)

def sixPtdStar(sz):
    for i in range(2):
        
        triangle(sz)
        kokoro.pu()
        kokoro.fd(sz / 3)
        kokoro.rt(60)
        kokoro.fd(sz / 3)
        kokoro.pd()
        kokoro.lt(120)
    kokoro.rt(120)

def rowOfStars(numInRow,sz):
    for i in range (numInRow):
        sixPtdStar(sz)
    kokoro.rt(90)

def main(sz,numInRow):
    start()
    for i in range (4):
        rowOfStars(numInRow,sz)

main(72,6)
