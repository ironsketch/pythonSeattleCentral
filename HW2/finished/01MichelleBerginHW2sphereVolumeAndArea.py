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
