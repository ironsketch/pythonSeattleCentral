# Importing ascii lowercase letters
from string import ascii_lowercase

# Definition taking 2 parameters
def enc(char,shift):

    # If what the user submitted is not in ascii_lowercase
    if char not in ascii_lowercase:
        # Then return the char submitted rather then processing it
        return char
    # is it IS ascii_lowercase letter then:
    else:

        # Find the index location
        ndx = ascii_lowercase.find(char)

        # Getting the new location by the passed through shift value
        newNdx = (ndx + shift) % 26

        # Return answer of new letter from index location to def en()
        return ascii_lowercase[newNdx]

def en(plainTxt,shift):

    # setting up a black variable
    code = ''

    # For each char in the user submitted phrase
    for char in plainTxt:

        # Add the result from using the def enc
        code += enc(char,shift)

    # Return the result to be printed in main()
    return code

def main():

    # Gets user input
    plainTxt = input('Enter something to cipher ')

    # Calls the def en and passes the user input and my chosen shift
    print(en(plainTxt,4))

main()
