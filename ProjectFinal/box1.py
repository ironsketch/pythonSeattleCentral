colorList = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']
def randColor():
    color = randint(0,7)
    return color

## SIMPLE FIRST BOX ##

def triangleinBox(side):
    kokoro.begin_fill()
    kokoro.color(colorList[randColor()],colorList[randColor()])
    diagonal = side * sqrt(2)
    kokoro.rt(45)
    kokoro.fd(diagonal)
    kokoro.lt(135)
    kokoro.fd(side)
    kokoro.lt(135)
    kokoro.fd(diagonal)
    kokoro.rt(135)
    kokoro.fd(side)
    kokoro.rt(90)
    kokoro.end_fill()
    
    
def box(boxLength,n,side,color):
    kokoro.begin_fill()
    kokoro.color(colorList[randColor()],colorList[randColor()])
    for i in range(4):
        kokoro.fd(side)
        kokoro.rt(90)
    kokoro.end_fill()
    triangleinBox(side)

def rowOfBoxes(boxLength,n,side,iteration):
    for i in range(n):
        box(boxLength,n,side,i + iteration)
        kokoro.pu()
        kokoro.fd(side)
        kokoro.pd()

def allBoxes(boxLength,n):
    side = boxLength / n
    for i in range(n):
        rowOfBoxes(boxLength,n,side,i)
        kokoro.pu()
        kokoro.rt(90)
        kokoro.fd(side)
        kokoro.lt(90)
        kokoro.back(boxLength)
        kokoro.pd()

## END SIMPLE FIRST BOX ##
