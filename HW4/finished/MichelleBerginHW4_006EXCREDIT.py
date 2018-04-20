'''[Extra Credit] Write a program which uses a dictionary that
reads in a file, gettysberg.txt , that I provide and  which prints
out the number of occurrences of each character in the file.'''

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


