#YouTube https://youtu.be/_MDP0PqJhBo
################################################
##                  YouTube                   ##
################################################

from math import *

# To calculate Circumference of circle with 1 parameter passed in
def CircumOfCircle(R):
    C = (R * 2) * pi
    return C

# To calculate Area of circle with 1 parameter passed in
def AreaOfCircle(R):
    A = pi * R**2
    return A

# To calculate area of cylinder with 2 parameters passed in
def AreaOfCylinder(R,h):
    AreaC = (2 * pi * R * h) + (2 * pi * (R**2))

    # Printing out result
    print ('The total area of a cylinder of radius',R)
    print('and height',h,'is',AreaC,'square units.')

def DoThis():

    # Calling each def to process a bit of each info
    print(AreaOfCircle(1))
    print(CircumOfCircle(1))
    AreaOfCylinder(1,2)
    AreaOfCylinder(2,1)

DoThis()
