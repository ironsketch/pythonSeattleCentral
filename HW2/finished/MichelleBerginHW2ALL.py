# Problems: #01,#02,#03,#04,#05,#06,#07,#08,#09,#10,#11,#YouTube
# YouTube Link:
# https://www.youtube.com/watch?v=ojv6HRkk4XQ  #

#01
################################################
##             Sphere Calculation             ##
################################################

# Importing the math library for python in order to use things like math.pi or in other words yummy pie.
import math

# Setting up the variable radius to collect the nessecary data for calculating area and volume.
radius = eval(input('Enter in a sphere\'s radius: '))

# Creating a function called calcSphere with a parameter for input. 
def calcSphere(radius):

    # Below is using the input for the parameter, radius, to calculate both area and volume.
    area = 4*math.pi*(radius**2)
    volume = (4/3)*math.pi*(radius**3)

    # Printing out the results.
    print ('The area of your circle with the radius at, ',radius,' is: ',area)
    print ('The volume of your circle with the radius at, ',radius,' is: ',volume)

# Calling the definition calcSphere and inputing the parameter radius with what the user inputed.
calcSphere(radius)

#02
################################################
##              Konditorei Coffee             ##
################################################

# Friendly printout to tell you where you are.
print('Welcome to the Konditorei Coffee ordering program')

# Empty space
print()

# Submitting user input into variable pounds
pounds = eval(input('How many pounds of coffee will satiate your needs?: '))

# Definition to calculate cost with 1 parameter
def calcCost(pounds):

    # Calculate just the per pound cost
    coffeeCost = (pounds * 10.50)

    # Calculate shipping cost
    shippingCost = (pounds * .86) + 1.50

    # Adding both together to give customer total cost with coffee and shipping
    totalCost = coffeeCost + shippingCost

    # Print out of totals so customer is aware of impending doom
    print ('Your total cost for everything is: ${totalCost:.2f}'.format(**locals()))
    print ('Your total cost for coffee is: ${coffeeCost:.2f}'.format(**locals()))
    print ('Your total cost for shipping is: ${shippingCost:.2f}'.format(**locals()))

# Calling definition calcCost with input of one parameter as defined by user
calcCost(pounds)

#03
################################################
##         Difference of 2 Points             ##
################################################

# Importing math in order to use sqrt()
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

#04
################################################
##             Average of Numbers             ##
################################################

# Creating the main definition
def main():

    # Telling the user what this does
    print('This will calculate the average of your numbers')

    # Initializing how many times we will need to run a loop to gather data
    times = eval(input('How many numbers will you be inputting?: '))

    # Initializing variable to add all numbs together
    allTogether = 0

    # For loop in the range defined by user, earlier
    for i in range (times):

        # Asking for input from user each time it runs through
        num = eval(input('Enter your number: '))

        # Adding to allTogether that number which started at 0
        # Each itteration adding a new number submited by user
        # To it's self, allTogether
        allTogether += num

    # Dividing all the added numbers by time number of times
    # The user previously stated
    allTogether /= times

    # Printing divded number
    print('\nThe sum for all yer numbers is: ', allTogether)

# Calling main method
main()

#05
################################################
##                  Appx pi                   ##
################################################

# Importing math, if I didn't I wouldn't be able to use math.pi later
import math

# Creating main def
def main():

    # Explaining to user what this does
    print('This will approximate pi with the algorithm:')
    print('4/1 - 4/3 + 4/5 - 4/7 + 4/9 ...etc...')

    # Asking user to run this a nth number of times
    times = eval(input('How many terms shall I use?: '))

    # Establishing two variables to be used
    adder = 0.0
    sign = 1.0

    # Running this nth number of times defined by user
    # Running this an even number of times to ensure
    # that last variable is negative so that we may
    # switch the sign in the end.
    # Using sign as defined above with algorythim to
    # Keep flipping the sign 4/1 (-4/3) etc.
    # Running denom in steps of 2 as defined by the
    # Algorithm for approximating pi above.
    for denom in range(1, 2*times, 2):

        # Adding the result of 4 dvided by the denominator
        # That is being incrimented each time by 2 and
        # timesing that number by 1 or - 1 depending on itteration
        adder += sign * 4.0/denom

        # Swapping the sign to adhere to the algorithm
        sign = -sign

    # Printing out the approximation
    print('\nThe approximation to pi is: ', adder)

    #Printing how close it came to mimicing math.pi
    print('The difference from math.pi is: ', math.pi - adder)

# Calling main method
main()

#06
################################################
##           Triangle Possibility             ##
################################################

# Creating a definition that takes in 3 parameters
def isTriangle(a,b,c):

    # Creating an if/else statement
    # If any of these conditions are met then print
    if a >= b + c or b >= a + c or c >= a + b:
        print('This triangle is not possible, you FOOL!')
    # Otherwise all others print this
    else:
        print('This is a lovely little triangle')

# Calling the def isTriangle 3 times. Each time testing
# the outcome
isTriangle(3,4,5)
isTriangle(2,2,2)
isTriangle(2,3,5)

#07
################################################
##             Evens From List                ##
################################################

# Creating a def called, evensFromList that uses one parameter, listed
def evensFromList(listed):

    # Telling the user what is happening
    print('This will only print out the even numbers in a given int list.')

    # Creating a for loop using the list put in by the parameter
    # listed and traversing it with i
    for i in listed:

        # If the remainder left by dividing 2 in to the number
        # equals 0, then print the number with no ending line
        if i % 2 == 0 :

            # Printing each number with no new line character
            # Overiding what is by default a \n with _ one space
            print(i, end=' ')

    # Sometimes using end will have the program wait for next line
    # (how python knows to keep going) To combat that, printing
    # another line
    print('\nAll the EVENS!')

# Calling definition evensFromList and submitting one parameter,
# a list with range 10 numbers 0 - 9
evensFromList(list(range(10)))

#08
################################################
##                 NegNonNeg                  ##
################################################

# Setting up the two lists to append to out side all functions
# So that they can be seen by all... scope?
negative = []
positive = []

# Creating a seperate definition to handle sorting
def sort(l):

    # Traversing through the list submitted as a parameter
    # Designated by l
    for i in l:

        # If i is less than 0, it has to be negative
        if i < 0:

            # Appending those mean negatives to a list called negative
            negative.append(i)

        # Which means all other possibilities are either + or 0
        else:

            # Appending the wayward +'s to a list called positive
            positive.append(i)

# Creating a main function to run the main program
def main():

    # Telling the user what we 'bout to do
    print('This will sort out all your negative numbers')
    print('and all your positive numbers into 2 lists')

    # Commanding the user to obey. Entering a list of numbers
    # Which python is so kind to already know to treat it as a list!
    sortme = eval(input('Enter numbers seperated only by commas: '))

    # Passing that new list, sortme, as a parameter to the def, sort
    sort(sortme)

    # Because I am lazy, printing the raw format of both lists
    print(negative)
    print(positive)

main()

#09
################################################
##        Go Home Turtle, you're drunk.       ##
################################################

# Importing turtle library
import turtle

# Importing specifically random integer from random library
from random import randint

# Importing all things from math
from math import *

# Declaring my window
wn = turtle.Screen()

# Setting my window BGcolor
wn.bgcolor('Dark Slate Gray')

# My title! It appears in the window top bar
wn.title('Go Home Turtle, You\'re DRUNK!')

# Assigning my turtle a name kokoro (variable)
kokoro = turtle.Turtle()

# Setting up my turtle color! which also sets line color
# which can also be changed too
kokoro.color('Medium Turquoise')
kokoro.speed(0)

# Setting up the main def for my drunk turtle
def drunkTurtle():

    # Setting up this variable to be used later
    d = 0

    # Setting up counter
    times = 1

    # Setting up list of colors
    colorList = ['Purple','Deep Pink','Red','Dark Orange','Yellow','Lime Green','Deep Sky Blue','Midnight Blue']

    # While statement, in the while statement we use the
    # squaring to get rid of - sign and then we compare
    # the result to see if it is greater than 200. If it
    # Is then we stop the turtle because the while
    # statement ends.
    while d <= 200:

        # Random int from 0 - 359
        randomNum = randint(0,359)
        color = randint(0,7)

        # Move kokoro forward 10
        kokoro.fd(10)

        # Pick up pen
        kokoro.pu()

        # Move forward 10
        kokoro.fd(10)

        # Put down pen
        kokoro.pd()

        # Left turn at random number
        kokoro.lt(randomNum)

        # Getting kokoro's position and simultaneously
        # assigning variables accordingly
        x,y = kokoro.pos()

        # Stopping Kokoro at radius d in the while loop
        d = sqrt(x**2 + y**2)

        # Counter to see how many times kokoro will move
        times += 1
        kokoro.pencolor(colorList[color])
        
    print (times)

# Calling main def
drunkTurtle()


#10
################################################
##             Fibonacci Sequence             ##
################################################

# The Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.

# Based on definition provided by Google, I am going to attempt
# this without looking at the HW 2 Solns_1.py
def fib():

    # Assigning Variables
    aNum = 0
    bNum = 1
    cNum = 1

    # Printing first variables
    print(aNum)
    print(bNum)
    print(cNum)

    # Running through Fibonacci sequence 10 times
    # Clunky and stupid. Not nice like the teachers
    # I make each number add the last two that were
    # just added and I run that 10 times
    for i in range (10):
        aNum = bNum + cNum
        print(aNum)
        bNum = aNum + cNum
        print(bNum)
        cNum = aNum + bNum
        print(cNum)

# Calling def fib
fib()

#11
################################################
##             Fibonacci Sequence             ##
################################################
## This doesnt work like it should.... sorry
from math import *

n = eval(input('Enter a number '))
times = eval(input('How many iterations '))
for i in range(times):
    newt = 2 / n
    newton = (newt + n) / 2
    n = newton
    print(newton)


#YouTube
################################################
##               YouTube Spiral               ##
# https://www.youtube.com/watch?v=ojv6HRkk4XQ  #
################################################

# Importing the turtle library
import turtle

# Setting up my window
wn = turtle.Screen()

# Setting the color of my window
wn.bgcolor('Dark Slate Gray')

# Setting the title of my windpw
wn.title('Kokoro saves your heart')

# Setting up my turtle a kokoro which stores library information
# from turtle into the variable turtle so that when I assign things
# for turtle to do it knows where to find the def's: in turtle
kokoro = turtle.Turtle()

# Setting my turtle color
kokoro.color('Medium Turquoise')

# My main def
def main():

    # I didn't want to make two different .py files so I am asking what direction
    # spira the user would like and setting an if else statement to organize
    bigOrSmall = input('Do you want the spiral getting bigger or smaller? (big/small): ')

    # If the user has typed small (and all lower case correct spelling) it will run this:
    if bigOrSmall == 'small':

        # Collecting data of how wide to start the spiral
        length = eval(input('How long do you want the start of the spiral to be?: '))

        # Asking what increment of change they would like
        changeInLength = eval(input('How much of a change in length would you want?: '))

        # And how many sides. I haven't made this program work well with too many sides
        sides = eval(input('How many sides would you like?: '))

        # Too translate their side option into degrees
        sides = 360 // sides

        # Sending the data to the def Small
        spiralSmall(length,changeInLength,sides)
    else:
        length = eval(input('How long do you want the start of the spiral to be?: '))
        changeInLength = eval(input('How much of a change in length would you want?: '))
        sides = eval(input('How many sides would you like?: '))
        sides = 360 // sides
        spiralBig(length,changeInLength,sides)

# Def small with 3 parameters
def spiralSmall(length,changeInLength,sides):

    # Spiral for 20 times with for statement and range
    for i in range(20):
        
        # Move forward length number of times
        kokoro.fd(length)

        # From calculated degree, turn left
        kokoro.lt(sides)

        # Move forward again 
        kokoro.fd(length)

        # Turn left again 
        kokoro.lt(sides)

        # Increasing by user defined change in length to spiral
        length += changeInLength
        
def spiralBig(length,changeInLength,sides):

        for i in range(20):

            # Just so the turtle doesnt start going backwards
            # I have a while statement that if the turtle gets
            # smaller in length than the change in length it stops
            while length >= changeInLength:
                kokoro.fd(length)
                kokoro.lt(sides)
                kokoro.fd(length)
                kokoro.lt(sides)

                # Minusing the change in length from the original
                length -= changeInLength

# Calling the main method
main()
