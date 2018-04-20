import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')

def dashedLine():
    for i in range(10):
        kokoro.fd(10)
        kokoro.pu()
        kokoro.fd(10)
        kokoro.pd()

dashedLine()
