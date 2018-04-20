from graphics import *
win = GraphWin('SkipBo', 600, 800)
win.setBackground("Light Steel Blue")
mouseSearch = True

while mouseSearch == True:
    mouseLocation = win.getMouse()
    print(mouseLocation.getX(),mouseLocation.getY())
