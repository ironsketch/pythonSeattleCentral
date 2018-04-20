import turtle

def fillSqrWclr(s,ls,lc,fc):
    '''Draws a square
size = s,  line size = ls, line color = lc, fill color = fc
'''
##    wn = turtle.Screen()
##
##    wn.bgcolor("lightgreen") # Set the window background color
##    wn.title("Tess draws colored sqr") # Set the window title
    tess.color(lc,fc) # lc is line color.   fc is fill color.
    tess.pensize(ls) # Tell tess to set her pen width
    tess.pu() # pick up pen
    # put pen in lower lefthand corner
    tess.bk(s/2)
    tess.lt(90)
    tess.bk(s/2)
    tess.rt(90)
    # turn to start square
    tess.pd() # put pen down
    tess.begin_fill()
    for i in range(4): #draw square
        tess.fd(s)
        tess.lt(90)
    tess.end_fill()
    tess.pu() # pick up pen
    # move back to center
    tess.lt(90)
    tess.fd(s/2)
    tess.rt(90)
    tess.fd(s/2)
    tess.pd() # leave pen down
    
wn = turtle.Screen()
wn.bgcolor("lightgreen") # Set the window background color
wn.title("Tess draws colored sqr") # Set the window title
tess = turtle.Turtle()

fillSqrWclr(150,5,"blue","yellow")
