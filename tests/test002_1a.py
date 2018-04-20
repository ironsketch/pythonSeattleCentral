import math
def circleArea(r):
    area = math.pi * (r**2)
    return area

def circum(r):
    circF = 2 * math.pi * r
    return circF

def cylinderArea(r,h):
    topBottom = circleArea(r) * 2
    side = circum(r) * h
    total = topBottom + side
    return total

def main():
    print('  Radius (cm)\tArea (cm)\tCylinder Area (cm^2)')
    print('\t-----   -----   \t---------------')
    r = 5.0
    h = 10
    for i in range(10):
        
        print ('\t%.1f' % r, '\t %.f' % h, '\t\t%.3f' % cylinderArea(r,h))
        r += .1
    
    
main()


