# Problems: #01,#02,#03,#04,#05,#06,#07,#YouTube https://youtu.be/_MDP0PqJhBo

#01
################################################
##         Zelle 6.4.  sumN,sumNCubes         ##
################################################

# Takes one parameter and
def sumN(n):
    added = 0

    # Uses it as the range (+1 to get the actual total)
    for num in range(1,n + 1):

        # Adding the num from the range to the established variable
        added += num

    # Returns total added
    return added

# Takes one parameter and
def sumNCubes(n):
    added = 0

    # Uses it as the range (+1 to get the actual total)
    for num in range(1,n + 1):

        # First I cube each num
        cubed = num**3

        # And THEN I added it to the variable
        added += cubed

    # Then I return the total sum
    return added

def main():

    # Taking info from user
    userNum = eval(input('Please enter a number > than 0 and not a float: '))
    print('Your number with all previous natural numbers added up is:')

    # Calls definition and sends one parameter (user input)
    print(sumN(userNum))
    print('Your numbers cubed and added up')

    # Calls definition and sends one parameter (user input)
    print(sumNCubes(userNum))

main()

#02
################################################
##            Zelle 6.10 – acronym            ##
################################################

# Definition to process the user input with 1 parameter
def acro(userString):

    # Initializing variable to store acronym
    acronym = ''

    # Splitting the string with spaces
    manipulate = userString.split(' ')

    # Running through each word that was split
    for word in manipulate:

        # Taking the first character of each word and appending
        # it to acronym
        acronym += word[0]

    # Returning the result and making it uppercase
    return acronym.upper()

def main():

    # Getting user input
    userString = input('Enter in a phrase: ')

    # Printing result of passed data
    print(acro(userString))

main()

#03
################################################
##          Zelle 6.11 - squareEach           ##
################################################

L = [1,4,55,6,84,34,2,354,4365,3,54776]

# Definition to process list (1 parameter)
def squareEach(nums):

    # Initializing a counter to use as location in List
    counter = 0

    # Iteration through items in list nums
    for number in nums:

        # updating number to be the square of it's self
        number = number**2

        # Using counter to insert the updated value back into
        # the same location in List
        nums[counter] = number

        # Plusing counter
        counter += 1

    # Printing new result
    print (nums)

def main():

    # Printing before
    print(L)

    # Sending one parameter to process
    squareEach(L)

main()

#04
################################################
##          Zelle 6.13 - toNumbers            ##
################################################

# Setting up a dictionary to easily switch from the text
# format of a number to it's int equivalence
numbDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12};

# The initial List to modify
L = ['one','two','three','Four','five','ten','sIX','seven']

# The def that will manipulate list (1 param)
def toNumbers(List):

    # Initializing counter for use in updating List
    counter = 0

    # Iterating through the list to modify each entry
    for item in List:

        # Updating item to reflect the corrasponding result
        # of each dictionary lookup
        item = numbDict[item.lower()]

        # Updating the list to the new data
        List[counter] = item
        counter += 1

    # Returning the new List
    return List

# Printing the List before
print(L)

# updating the old list to the new one
L = toNumbers(L)

# Printing the new one
print(L)

#05
################################################
##          Zelle 6.14 – compute sum          ##
################################################

def add(List):
    added = 0

    # Going through the list from before to add all num up
    for num in List:
        added += num
    return added

def openAndProcess(fileINnums):
    L = []

    # Opening file to read
    fileIN = open(fileINnums, "r")

    # Reading initial line
    line = fileIN.readline()

    # While the line still has characters in it do the following
    while line != '':

        # Squaring the evaluated line
        squared = eval(line)**2

        # Appending that to the list
        L.append(squared)

        # Reading next line
        line = fileIN.readline()

    # Closing the file
    fileIN.close()
    return L

def openAndAppend(final,fileName):

    fileOPEN = open(fileName,'w')
    print(final, file = fileOPEN)
    fileOPEN.close()

def main():

    # Getting user input of file name
    fileINnums = input('Type the name of your file and ext: ')

    # Sending that to open and process the info and storing the
    # result in variable listOfNums
    listOfNums = openAndProcess(fileINnums)

    # Adding all the numbers from before up
    finalTotal = add(listOfNums)

    # Opening and writing to file the new result
    openAndAppend(finalTotal,fileINnums)

main()

#06
################################################
##             6.  [Extra Credit]             ##
################################################

#Establishing the dict
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
           , 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0
           , 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0
           , 'y': 0, 'z': 0};

def openFile(letters):

    # Opening file to read
    fileIN = open('gettysberg.txt', "r")

    # Reading each line of the document
    line = fileIN.readline()

    # As long as the line is NOT blank do
    while line != '':

        # For each character in the line do
        for letter in line:

            # If that character is in the dict letters do
            if letter in letters:

                # For that key add one to it
                letters[letter] += 1
        # Read next line
        line = fileIN.readline()

    # Close Doc
    fileIN.close()
    print(letters)

openFile(letters)

#07
################################################
##             7.  [Extra Credit]             ##
################################################


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
