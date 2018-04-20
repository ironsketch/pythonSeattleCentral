import turtle

wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
turtle.setup(600, 600)
kokoro.speed(0)

def startingPoint():
    kokoro.pu()
    kokoro.setpos(-280,240)
    kokoro.pd()

def square(size):
    for i in range(4):
        kokoro.fd(size)
        kokoro.lt(90)

def fillColor(numb):
    if numb % 2 == 0:
        color = 'Red'
        return color
    else:
        color = 'Black'
        return color

def filler(i,size):
    kokoro.color(fillColor(i),fillColor(i))
    kokoro.begin_fill()
    square(size)
    kokoro.end_fill()

def rows(size,n):
    for i in range (n):
        filler(i,size)
        kokoro.fd(size)
        
def columns(poop):
    kokoro.rt(90)
    kokoro.pu()
    kokoro.fd(poop)
    kokoro.lt(90)
    kokoro.pd()
    
def main(size,n):
    columnSize = 51
    startingPoint()
    for i in range (1,8):
        
        rows(size,n)
        startingPoint()
        columnSize = columnSize * i
        columns(columnSize)

main(51,11)
