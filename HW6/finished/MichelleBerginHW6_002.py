#02
################################################
##                  Zelle 8.2                 ##
################################################
from math import *

def wCI():

    # Setting up all the variables
    T = -20
    V = 0

    # Printing with nice formating what I have done
    print('{:<10} {:<10} {:<10}'.format('Degree ','Wind Speed ','Wind Chill'))

    # Setting up something to run through the numbers and using it for
    # Wind Speed
    for i in range(0,50,5):

        # Breaking apart the math
        V = i**.16
        wind1 = 0.6215 * T
        wind2 = 35.75 * V
        wind3 = .4275 * T * V
        windChillIndex = 35.74 + wind1 - wind2 + wind3
        print('{:<10.3f} {:<10.3f} {:<10.3f}'.format(T,V,windChillIndex))
        T += 10
wCI()
