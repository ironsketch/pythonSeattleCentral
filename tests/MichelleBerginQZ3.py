## OVERALL GRADE = 62.5/52.5

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

def triangle(sz,num):
    for i in range (3):
        if num % 2 == 0:
            kokoro.pencolor('Red')
        else:
            kokoro.pencolor('Black')
        kokoro.fd(sz)
        kokoro.lt(120)

def sixPtdStar(sz, num):
    for i in range(2):
        num += i
        triangle(sz,num)
        kokoro.pu()
        kokoro.fd(sz / 3)
        kokoro.rt(60)
        kokoro.fd(sz / 3)
        kokoro.pd()
        kokoro.lt(120)
    kokoro.rt(120)
        
def rowOfStars(numInRow,sz):
    for i in range (numInRow):
        sixPtdStar(sz, i)
    kokoro.rt(90)

def main(sz,numInRow):
    start()
    for i in range (4):
        rowOfStars(numInRow,sz)

main(72,6)
