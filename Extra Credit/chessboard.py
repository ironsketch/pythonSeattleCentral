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

def square(size,color):
    kokoro.begin_fill()
    if color % 2 == 0:
        kokoro.color('Red','Red')
        for i in range(4):
            kokoro.fd(size)
            kokoro.lt(90)
    else:
        kokoro.color('Black','Black')
        for i in range(4):
            kokoro.fd(size)
            kokoro.lt(90)
    kokoro.end_fill()

def rowSquare(size,num,color):
    for i in range(num):
        square(size,color)
        kokoro.fd(size)
        
def newRowSetUp(size,num):
    kokoro.pu()
    kokoro.back(size * num)
    kokoro.rt(90)
    kokoro.fd(size)
    kokoro.lt(90)
    kokoro.pd()
    color += 1
    return color
    

def main(size,num):
    color = 0
    for i in range(num):
        rowSquare(size,num,color)
        color = newRowSetUp(size,num)
        
start()
main(45,8)
