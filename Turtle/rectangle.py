import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')
kokoro.pensize(.5)
L = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue','Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']

def rectangle(w,h):
    for x in range (2):
        cycle(w,h)
            

def cycle(w,h):   
    kokoro.fd(w)
    kokoro.lt(90)
    kokoro.fd(h)
    kokoro.lt(90)

def windmill(w,h,trnNgle):
    counter = 0
    for i in range (360 // trnNgle):
        color = L[counter]
        kokoro.pencolor(color)
        rectangle(w,h)
        kokoro.lt(trnNgle)
        counter += 1
        
windmill(20,100,30)
