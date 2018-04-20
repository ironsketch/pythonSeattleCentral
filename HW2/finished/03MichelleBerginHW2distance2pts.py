# Importing math in order to use sqrt()
import math 

def main():
    # Printing to user what app is about
    print('Find the distance between 2 points.')

    # simultaniously taking input from user and putting in sequential order each to the variable to the left
    x1,x2,y1,y2 = eval(input('Please enter your X1,X2,Y1,Y2 in that order: '))

    # The calculation of the x and y inputs to find distance
    # The result is stored in num
    num = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # The result printed out for the user with a truncation of the decimal point at 2 places
    print('The distance is: {num:.2f}'.format(**locals()))
main()
