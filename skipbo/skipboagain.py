from graphics import *

##mouseCheck = True

# Variables
skipboNum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
user1Deck = []
user2Deck = []
user1Hand = []
user2Hand = []
deckSize = 0
handCount = 5
x1 = 50
y1 = 60
x2 = 140
y2 = 210

win = GraphWin('SkipBo', 600, 800)
win.setBackground("Light Steel Blue")
quitbutt = Text(Point(590,795), 'Quit')
quitbutt.setFill('white')
quitbutt.setOutline("Light Steel Blue")
quitbutt.draw(win)

##while mouseSearch == True:
##    mouseLocation = win.getMouse()
##    print(mouseLocation.getX(),mouseLocation.getY())

def cards(pl1,pl2,x1,y1,x2,y2,ran):
    for i in range (ran):
        card = Rectangle(Point(x1,y1),Point(x2,y2))
        card.setFill('white')
        card.draw(win)
        x1 += pl1
        x2 += pl2

def start():
    started = Text(Point(95,320), 'Click to Start')
    started.setTextColor('Steel Blue')
    started.setStyle('bold')
    started.draw(win)

def main():
    title = Text(Point(300, 25), 'SkipBo')
    title.setSize(30)
    title.setTextColor('Steel Blue')
    title.draw(win)
    cards(100,100,150,y1,240,y2,4)
    cards(100,100,x1,440,x2,590,5)
    cards(5,5,30,250,120,400,5)
    start()
def quiter():
    win.getMouse()
    if (((getX() >= 588) and (getX() <= 592)) and ((getY() >= 793) and (getY() <= 799))):
        win.close()

main()
quiter()

