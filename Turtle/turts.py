import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')
def circleLTurn (size):
    for i in range(180):
        kokoro.fd(size)
        kokoro.lt(2)
def circleRTurn (size):
    for i in range(180):
        kokoro.fd(size)
        kokoro.rt(2)
def nextCircle1 (move):
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(move)
    kokoro.rt(90)
    kokoro.fd(move)
    kokoro.lt(90)
    kokoro.pd()

def first(size):
    circleLTurn (size)
    nextCircle1(59)
    circleRTurn (size)
    nextCircle1(58)
def second(size):
    circleRTurn (size)
    nextCircle1(59)

first(2)
for i in range (3):
    second(2)
def smaller(move):
    kokoro.pu()
    kokoro.lt(90)
    kokoro.fd(move)
    kokoro.rt(135)
    kokoro.fd(move)
    kokoro.lt(45)
    kokoro.pd()
smaller(30)
first(.5)



    
