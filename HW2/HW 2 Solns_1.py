# 1
# # # # # # # # # #
# c03ex01.py
#    Volume and serface area of a sphere
import math
def main():
    print("This program computes the volume and surface area of a sphere")
    print()

    r = eval(input("Please enter the radius of the sphere: "))
    volume = 4.0/3.0 * math.pi * r**3
    area = 4 * math.pi * r**2

    print("The volume is", volume, "cubic units.")
    print("The surface area is", area, "square units.")
main()
# >>>
# This program computes the volume and surface area of a sphere
#
# Please enter the radius of the sphere: 10
# The volume is 4188.790204786391 cubic units.
# The surface area is 1256.6370614359173 square units.
# >>>

# 2
# # # # # # # # # #
# c03ex05.py
#   Calculate the price of coffee shipments
#   Note: output is ugly. Chapter 4 covers formatting.
def main():
    print("Welcome to the Konditorei!")
    print()

    amount = eval(input("How many pounds of coffee do you want? "))
    coffeeCost = 10.5 * amount
    shipping = 0.86 * amount + 1.5

#     print()
#     print("Cost of coffee:", coffeeCost)
#     print("Shipping:      ", shipping)
#     print("-------------------------------")
#     print("Total due:     ", coffeeCost + shipping)

    print()
    print('Cost of coffee: ${coffeeCost:.2f}'.format(**locals()))
    print('Shipping:       $ {shipping:.2f}'.format(**locals()))
    print("-------------------------------")
    temp = coffeeCost + shipping
    print('Total due:      ${temp:.2f}'.format(**locals()))
main()
# >>>
# Welcome to the Konditorei!
#
# How many pounds of coffee do you want? 12
#
# Cost of coffee: $126.00
# Shipping:       $ 11.82
# -------------------------------
# Total due:      $137.82
# >>>

# 3
# # # # # # # # # #
# c03ex07.py
#    Calculates the distance between two points
import math
def main():
    print("This program calculates the distance between two points.")
    print()
    x1, y1 = eval(input("Enter coordinates of the first point (x,y): "))
    x2, y2 = eval(input("Enter coordinates of the second point(x,y): "))
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print()
    print("The distance between the points is", distance)
main()
# >>>
# This program calculates the distance between two points.
#
# Enter coordinates of the first point (x,y): 1,2
# Enter coordinates of the second point(x,y): 4,6
#
# The distance between the points is 5.0
# >>>

# 4
# # # # # # # # # #
# c03ex14.py
#    Average of numbers entered by the user.
def main():
    print("Program to calculate average")
    print()
    n = eval(input("How many numbers do you have? "))
    sum = 0
    for i in range(n):
        num = eval(input("Enter a number: "))
        sum = sum + num
    print()
    print("The average of the numbers is:", sum/n)
main()
# >>>
# Program to calculate average
#
# How many numbers do you have? 5
# Enter a number: 2
# Enter a number: 4
# Enter a number: 6
# Enter a number: 8
# Enter a number: 10
#
# The average of the numbers is: 6.0
# >>>

# 5
# # # # # # # # # #
# c03ex15.py
#    Approximation of pi using Taylor series.
import math
def main():
    print("This program approximates the value of pi by summing a fixed")
    print("number of terms in a series.")
    print()
    n = eval(input("How many terms should I use? "))
    sum = 0.0
    sgn = 1.0   # used to alternate sign of terms
    for denom in range(1, 2*n, 2):
        sum = sum + sgn * 4.0/denom
        sgn = -sgn #flip the sign
    print("Approximation to pi is:", sum)
    print("Difference from math.pi:", math.pi - sum)
main()
# >>>
# This program approximates the value of pi by summing a fixed
# number of terms in a series.
#
# How many terms should I use? 10
# Approximation to pi is: 3.0418396189294032
# Difference from math.pi: 0.09975303466038987
# >>> main()
# This program approximates the value of pi by summing a fixed
# number of terms in a series.
#
# How many terms should I use? 250
# Approximation to pi is: 3.137592669589472
# Difference from math.pi: 0.0039999840003210885
# >>> main()
# This program approximates the value of pi by summing a fixed
# number of terms in a series.
#
# How many terms should I use? 1000
# Approximation to pi is: 3.140592653839794
# Difference from math.pi: 0.000999999749998981
# >>>
# 6

def is_triangle(a,b,c):
    '''
takes three integers as arguments,
prints either 'Triangle Possible' or 'Triangle Not Possible'
depending on whether you can
or cannot form a triangle from sticks with the given lengths.
Uses booleans   and    or   not
'''
    if a >= b+c    or b >= a + c    or c >= a + b:
        print("Triangle Not Possible")
    else:
        print("Triangle Possible")
#>>> is_triangle(3,4,5)
#Triangle Possible
#>>> is_triangle(2,2,2)
#Triangle Possible
#>>> is_triangle(2,3,5)
#Triangle Not Possible
#>>> 

# # 7
def evensFromList(ints):
    '''
    Takes a list of ints & prints out the even numbers
    from the list.
    '''
    print('The even numbers from the list are: ')
    for num in ints:
        if num % 2 == 0:
            print(num)

# >>> evensFromList(list(range(10)))
# The even numbers from the list are:
# 0
# 2
# 4
# 6
# 8
# >>>

# 8
def negNonNeg(nums):
    '''
    nums is a list of numbers.
    prints out 2 list:
        a list of neg nums
        a list of nonneg nums.
        '''
    negs = []
    nonNegs = []
    for num in nums:
        if num < 0:
            negs.append(num)
        else:
            nonNegs.append(num)
    print('Negative numbers: ',negs)
    print('Non negative numbers: ',nonNegs)

# >>> negNonneg(list(range(-5,5,1)))
# Negative numbers:  [-5, -4, -3, -2, -1]
# Non negative numbers:  [0, 1, 2, 3, 4]
# >>>

#  9
import turtle
from random import randint
from math import sqrt

def ranWalk():
    '''
    . Use the turtle module and the random module to make
    the turtle execute a random walk using a length of ten
    for each step.  The turtle will stop the first time it
    gets 200 steps or greater from its start.  Generate a
    record of the turtle moving on the canvas and print out
    in the shell the number of turtle moves taken before it
    stops.  Run your program 3 times.
    '''
    wn = turtle.Screen() # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    wn.title("tess is drunk")
    tess = turtle.Turtle() # Create tess and set some attributes
    tess.color("hotpink")
    tess.pensize(5)
    # draw circle
    tess.pu();tess.fd(200);tess.pd();tess.lt(90);tess.circle(200);tess.rt(90)
    tess.pu();tess.bk(200);tess.pd()
    tess.color('blue')
    d = 0
    stepNum = 1
    while d < 200:
        tess.fd(50)
        x,y = tess.pos()
        d = sqrt(x**2 + y**2)
        print('step number',stepNum,'position =',(round(x,1),round(y,1)),'distance from start =',round(d,1))
        tess.rt(randint(0,359))
        stepNum += 1
    wn.mainloop()

#ranWalk()
#
#>>>
#step number 1 position = (50.0, -0.0) distance from start = 50.0
#step number 2 position = (87.2, -33.5) distance from start = 93.4
#step number 3 position = (60.7, -75.9) distance from start = 97.1
#step number 4 position = (65.0, -26.0) distance from start = 70.0
#step number 5 position = (34.9, -66.0) distance from start = 74.7
#step number 6 position = (58.4, -21.8) distance from start = 62.3
#step number 7 position = (104.1, -1.5) distance from start = 104.1
#step number 8 position = (128.3, 42.2) distance from start = 135.1
#step number 9 position = (178.3, 42.2) distance from start = 183.3
#step number 10 position = (225.9, 26.8) distance from start = 227.5

# 10
# # # # # # # # # #
# c03ex16.py
#    Nth fibonacci number
def main():
    print("This program calculates the nth Fibonacci value.")
    print()
    n = eval(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    print()
    print("The nth Fibonacci number is", curr)
# main()
# >>>
# This program calculates the nth Fibonacci value.
#
# Enter the value of n: 5
#
# The nth Fibonacci number is 5
# >>> main()
# This program calculates the nth Fibonacci value.
#
# Enter the value of n: 50
#
# The nth Fibonacci number is 12586269025
# >>>

# 11
# # # # # # # # # #
# c03ex17.py
#    Square root using Newton's method.
import math
def main():
    print("This program calculates square root using Newton's method.")
    print()
    x = eval(input("Enter number to find the root of: "))
    n = eval(input("How many iterations should I use? "))
    guess = x / 2.0
    for i in range(n):
        guess = (guess + x/guess)/2.0
    print()
    print("Approximate square root:", guess)
    print("Difference from math.sqrt:", math.sqrt(x) - guess)
# main()
# >>>
# This program calculates square root using Newton's method.
#
# Enter number to find the root of: 5
# How many iterations should I use? 3
#
# Approximate square root: 2.2360679779158037
# Difference from math.sqrt: -4.1601389000334166e-10
# >>> main()
# This program calculates square root using Newton's method.
#
# Enter number to find the root of: 1000
# How many iterations should I use? 2
#
# Approximate square root: 127.49203187250995
# Difference from math.sqrt: -95.86925527082616
# >>> main()
# This program calculates square root using Newton's method.
#
# Enter number to find the root of: 1000
# How many iterations should I use? 5
#
# Approximate square root: 32.74064099486699
# Difference from math.sqrt: -1.1178643931832006
# >>> main()
# This program calculates square root using Newton's method.
#
# Enter number to find the root of: 1000
# How many iterations should I use? 10
#
# Approximate square root: 31.622776601683793
# Difference from math.sqrt: 0.0
# >>>
