from math import *

def distance(x2,x1,y2,y1):
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

def triangleArea(x1,y1,x2,y2,x3,y3):
    a = distance(x2,x1,y2,y1)
    b = distance(x3,x1,y3,y1)
    c = distance(x3,x2,y3,y2)
    s = (a + b + c)/2
    hf = sqrt(s * (s - a) * (s - b) * (s - c))
    return hf

def midPoint(x1,y1,x2,y2):
    mx = ((x1 + x2)/2)
    my = ((y1 + y2)/2)
    return mx,my

def main():
    x1,y1 = midPoint(0,0,3,4)
    x2,y2 = midPoint(0,0,3,0)
    x3,y3 = midPoint(3,4,3,0)
    print(triangleArea(x1,y1,x2,y2,x3,y3))

main()
