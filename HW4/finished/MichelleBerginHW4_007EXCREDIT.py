'''Write a program which uses a dictionary that  reads in a file,
gettysberg.txt, that I provide and  which prints out the  percent
relative frequency of each letter.  Percent relative frequency of
a letter is defined as  100 times the number of times that letter
occurs divided by the total number of letters.   Compare the letter
frequency you find from the file to that shown in
http://en.wikipedia.org/wiki/Letter_frequency  for the English language.'''

#07
################################################
##             7.  [Extra Credit]             ##
################################################


#Establishing the dict
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
           , 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0
           , 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0
           , 'y': 0, 'z': 0};

letterFreq = []

def openFile():

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

def main():
    openFile()
    for thing in letters:
        proc = thing * 100 / len(letters)
        
main()
