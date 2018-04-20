import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()

def dashedLine(length):
    for i in range(length):
        kokoro.pencolor('Medium Turquoise')
        kokoro.fd(10)
        kokoro.pu()
        kokoro.fd(10)
        kokoro.pd()
        kokoro.pencolor('White')
        kokoro.fd(10)
        kokoro.pu()
        kokoro.fd(10)
        kokoro.pd()

def dashedShape(length,angle):
    for i in range(length):
        kokoro.pencolor('Medium Turquoise')
        kokoro.fd(10)
        kokoro.pu()
        kokoro.lt(angle)
        kokoro.fd(5)
        kokoro.pd()
        kokoro.pencolor('White')
        kokoro.lt(angle)
        kokoro.fd(10)
        kokoro.pu()
        kokoro.lt(angle)
        kokoro.fd(10)
        kokoro.pd()

##length = eval(input('How many pixels do you want him to move?: '))
##length //= 20
##dashedLine(length)
for i in range (4):
    dashedLine(1)
    kokoro.goto(200, 100)
    dashedShape(5,45)
    kokoro.goto(200, -100)
