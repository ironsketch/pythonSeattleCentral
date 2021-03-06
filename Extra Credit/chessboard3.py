from math import *
import turtle

wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
##kokoro.speed(0)
kokoro.pensize(2)

def start():
    kokoro.pu()
    kokoro.bk(240)
    kokoro.lt(90)
    kokoro.fd(200)
    kokoro.rt(90)
    kokoro.pd()

def coloredSqr(sz,lc,fc):
    kokoro.pencolor(lc)
    kokoro.fillcolor(fc)
    kokoro.begin_fill()
    for i in range(4):
        kokoro.fd(sz)
        kokoro.lt(90)
    kokoro.end_fill()

def rowOfSquares(n,sz,lc1,fc1,lc2,fc2,num):
    for i in range (n):
        if num % 2 == 0:
            if i % 2 == 0:
                coloredSqr(sz,lc1,fc1)
            else:
                coloredSqr(sz,lc2,fc2)
        else:
            if i % 2 == 0:
                coloredSqr(sz,lc2,fc2)
            else:
                coloredSqr(sz,lc1,fc1)
        kokoro.pu()
        kokoro.fd(sz)
        kokoro.pd()

def chessBoard(n,sz,lc1,fc1,lc2,fc2):
    for i in range (n):
        rowOfSquares(n,sz,lc1,fc1,lc2,fc2,i)
        kokoro.pu()
        kokoro.back(n * sz)
        kokoro.rt(90)
        kokoro.fd(sz)
        kokoro.lt(90)
        kokoro.pd()

start()
chessBoard(8,45,'Red','Red','Black','Black')
