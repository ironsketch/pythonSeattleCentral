import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')
def square(width):
    for i in range(8):
        for i in range(4):
            kokoro.fd(width)
            kokoro.lt(90)
        kokoro.lt(45)

def petals():
    
    for i in range (5):
        kokoro.lt(20)
        kokoro.fd(150)
        kokoro.lt(40)
        kokoro.fd(20)
        kokoro.lt(135)
        kokoro.fd(20)
        kokoro.lt(20)
        kokoro.fd(150)

square(100)
petals()
