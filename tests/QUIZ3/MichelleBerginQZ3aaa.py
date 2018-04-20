from math import *
import turtle

wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.speed(0)

def start():
    kokoro.pu()
    kokoro.setpos(-240,220)
    kokoro.pd()
    

def rowOfStars(num,sz):
    for i in range (num):
        sixPtdStar(sz)
    
def triangle(sz):
    for i in range (3):
        kokoro.fd(sz)
        kokoro.lt(120)
    
def sixPtdStar(sz):
    for i in range(2):
        triangle(sz)
        length = sz / 3
        kokoro.fd(length)
        kokoro.rt(60)
        kokoro.fd(length)
        kokoro.lt(120)
    kokoro.rt(120)

def sqrOfRows(num,sz):
    for i in range(1):
        kokoro.bk(sz)
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(sz + 10)
        kokoro.lt(90)
        kokoro.pd()
        sixPtdStar(sz)

def main(num,sz):
    start()
    rowOfStars(num,sz)
    sqrOfRows(num,sz)
        
main(6,72)
