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


