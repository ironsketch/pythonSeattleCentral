# Problems: #01,#02,#03,#04,#05,#06,#07,#08,#08_w_sorted,#09,#10,#YouTube
# YouTube Link: https://youtu.be/836kybgGyoM
#   #

#01
################################################
##         Zelle 5.3 – computes grade         ##
################################################

def main():
    print('Find your exam grade')

    # Collecting grade from user
    score = eval(input('Enter your grade out of 100: '))

    # Basically an if elif statement because from what I can
    # understand, the variable grade is holding the letter
    # F, 60 times and D 10 times and C 20 etc. to 11 times A
    
    grade = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"

    # Then the [] is looking for the location based on the number
    # entered by the user to find the spot in the string where
    # the letter lies. So it is creating an if elif statement
    # but with less programming .... i think ....
    print('Your grade be',grade[score])

main()

#02
################################################
##        Zelle 5.4 – outputs acronym         ##
################################################

def main():

    # Setting up a blank variable
    acronym = ''

    # Getting the phrase from the user and it will be stored as a string
    phrase = input('Please input a phrase to make into an acronym. ')

    # I am going to process the string and split the words at the spaces
    # This turns it into a list
    process = phrase.split(' ')

    # Running through the list for each word
    for word in process:

        # Adding the first letter of each word to the variable acronym
        acronym += word[0]

    # Printing out the rest in upper case
    print(acronym.upper())
    
main()

#03
################################################
##        Zelle 5.5 – computes numeric        ##
################################################

def main():

    # Setting up a variable with the alphabet so that I can use it
    # to count 1 - 26 for the program (faster and less code)
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # Setting up a variable to start at 0
    added = 0

    # take in users word
    word = input('Please enter a word to calculate. ')

    # Iterating through all letters in the word entered
    for letter in word:

        # using place as a variable to store the index of the
        # letter found
        place = alpha.find(letter)

        # Adding it to the variable added. But adding 1 place
        # since an index starts at 0 not 1
        added += (place + 1)

    # Printing result
    print (added)

main()

#04
################################################
##       Zelle 5.6 - computes full name       ##
################################################

def main():

    # Setting up a variable with the alphabet so that I can use it
    # to count 1 - 26 for the program (faster and less code)
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # Setting up a variable to start at 0
    added = 0

    # take in users word
    fullName = input('Please enter your full name. ')

    # I am going to process the string and split the words at the spaces
    # This turns it into a list
    process = fullName.split(' ')

    # Iterating through all letters in the word entered
    for word in process:
        for letter in word:
            # using place as a variable to store the index of the
            # letter found
            place = alpha.find(letter)

            # Adding it to the variable added. But adding 1 place
            # since an index starts at 0 not 1
            added += (place + 1)

    # Printing result
    print (added)

main()

#05
################################################
##          Zelle 5.7 – Caesar cipher         ##
################################################

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

#06
################################################
##   Zelle 5.10 – computes avg word length    ##
################################################

def process(text):

    # We are splitting words by the spaces
    words = text.split(' ')

    # We return what was processed
    return words

def average(text):
    counter = 0
    wordCount = 0

    # We process what was sent in to seperate the words
    words = process(text)

    # For each word we will get the length and add that to a counter
    # We will also keep track of how many words we used
    for word in words:
        length = len(word)
        counter += length
        wordCount += 1

    # THen we will divide them to get our average
    counter /= wordCount

    # Returning the average to be printed for the user
    return counter

def main():
    print('Find your average word length')

    # Getting user input
    plainTxt = input('Enter a sentance: ')

    # Will print out answer after it is processed
    # The parameter passed through is the data from
    # the variable plainTxt
    print('Your average word length is: ', average(plainTxt))

main()

#07
################################################
##          Zelle 5.14  - word count          ##
################################################

def readingFile(fname):

    # Opening the file and reading it 'r'
    infile = open(fname, 'r')

    # Setting up the variable chars with what was in the doc
    chars = infile.read()

    # Closing the file
    infile.close()

    # Returning the doc stored in chars
    return chars

def countLines(lines):
    count = 0
    for line in lines:
        count += 1
    return count

def countWords(words):
    count = 0
    for word in words:
        count += 1
    return count

def main():

    # Sending the file name to be read. So if I wanted to make
    # this app do many files all I had to do was ask the user
    # what file they want
    doc = readingFile('worddoc.txt')

    # First splitting the doc by \n (new line)
    lines = doc.split("\n")

    # Sending the split lines to be counted
    lineCount = countLines(lines)

    # splitting the doc by spaces
    words = doc.split()

    # Sending the split words to be counted
    wordCount = countWords(words)

    # Printing out the result
    print('Your number of lines is: ',lineCount)
    print('Your number of words is: ', wordCount)
    
main()

#08
################################################
##     returns True if the list is sorted     ##
################################################

'''
8.  Write a function, is_sorted(L), which takes a list as a
    parameter & returns True if the list is sorted, OTW
    returns False.

    I am not quite sure what is being asked of me but I
    assume you are asking us to check to see if a list
    given is numerical or alphabetical that it is
    in numerical order or alphabetical order?
'''

# Setting up a false list
alphaList = ['apple','zears','dsshole']

# Setting up my comparitor to find if the order is alphabetical
alphaCheck = 'abcdefghijklmnopqrstuvwxyz'

# Setting up a false list (Will return False)
numCheck = [0,1,2,3,60,5,6,7,8,50]

# Checks to see if number is in order
def numOrder(check):
    indx = 0
    indx2 = 0

    # For number in the range of the list length
    for i in range (len(check)):

        # Assign indx to be what the first item in the list Check is
        indx = check[i]

        # If indx is bigger than or equal to indx2 (which at the
        # beginning it is designed to be) 
        if indx >= indx2:

            # Then assign indx2 with what indx is. That way the next
            # time around if what is in check is smaller than indx2
            # You will know that it is NOT in numerical order
            indx2 = indx
        else:

            # Returns false if the above conditions are met
            return False
    # Returns true if and only if all iterations of the List have been
    # completed without going to the else 
    return True

# Same idea as the above numerical one except I compare the letter to a
# string of alphabet and use the index to compare.
def alphaOrder(check):
    indx = 0
    indx2 = 0
    for item in check:
        indx = alphaCheck.find(item[0])
        if indx >= indx2:
            indx2 = indx
        else:
            return False
    return True
def main():
    print(numOrder(numCheck))
    print(alphaOrder(alphaList))

main()

#08_w_sorted
################################################
##     returns True if the list is sorted     ##
################################################

# Setting up a true list
alphaList = ['apple','bears','dsshole']

# Setting up a false list (Will return False)
numCheck = [0,1,2,3,60,5,6,7,8,50]

def is_sorted(L):

    # Sorts the given list into a new list, new
    new = sorted(L)

    # Does the old list and new equal each other?
    if new == L:

        # Yes return true
        return True
    else:

        # No return False
        return False

print(is_sorted(alphaList))
print(is_sorted(numCheck))

#09
################################################
##     9. Write a function, is_anagram(s1,s2) ##
##     , which takes 2 equal length strings & ##
##     returns True if they are anagrams, OTW ##
##     returns False.                         ##
################################################

# YES anagrams
ana1 = 'Old Hell Row'
ana2 = 'Hello World'

# NON anagrams
ana3 = 'Old Hell Row'
ana4 = 'Heglo World'

# Taking in 2 parameters
def is_sorted(ana1,ana2):

    # Removing spaces
    ana1 = ana1.replace(' ','')
    ana2 = ana2.replace(' ','')

    # Making sure they are all lower case and sorting them
    word1 = sorted(ana1.lower())
    word2 = sorted(ana2.lower())

    # Comparing them!
    if word1 == word2:
        return True
    else:
        return False

print(is_sorted(ana1,ana2))
print(is_sorted(ana3,ana4))

#10
################################################
##     10.  Write a function,                 ##
##     removeDupsFrom(L), which takes list    ##
##     as a parameter and returns a list      ##
##     with any duplicates removed.           ##
##     Write your function so that the        ##
##     original list is not modified.         ##
################################################

# My stupid list
L = [0,0,1,1,1,2,3,4,5,6,6,6,6,7,8,9,1,9,9,9,9,9,9,9]

L2 = ['bear','bear','cat']

def removeDupsFrom(L):

    # We don't want to somehow affect the original List
    # To stay on the safe side I will assign a new variable
    A = L

    # Iterate through all items in list A
    for item in A:

        # Count how many times each item appears
        count = A.count(item)

        # If there is more than 1
        if count > 1:

            # Then for each of itteration of that item
            # remove it from the list, minus 1. We don't
            # want to remove them all
            for i in range(count - 1):

                # The command to remove the item
                A.remove(item)
    # Returning the new list A to see that it is working
    return A

print(L)
print(removeDupsFrom(L))
print(L2)
print(removeDupsFrom(L2))

#YouTube https://youtu.be/836kybgGyoM
################################################
##                  YouTube                   ##
################################################

def readingFile(fname):

    # Opening the file and reading it 'r'
    infile = open(fname, 'r')

    # Setting up the variable chars with what was in the doc
    names = infile.read()

    # Closing the file
    infile.close()

    # Returning what was in that file to be used
    return names

def count(names):

    # Removing spaces so that they are not counted
    names = names.replace(' ','')
    counter = 0
    for name in names:
        for letter in name:
            # Adding for each iteration of character.
            counter += 1

    # Returning count
    return counter
    
        
    

def writeToFile(names):
    
    # Opening the file to overwrite it. If it doesn't exist
    # it is created
    namesAndNumVal = open('namesAndNumVal.txt','w')
    
    #sperating each line of info from the file to work with it
    names = names.split('\n')

    # Iterating through each line and writing to file. It's processing the
    # character length of each from count(l) and then writing it to file
    for l in names:
        print(l, ' ',count(l), file = namesAndNumVal)
        
    # Closing the file
    namesAndNumVal.close()

writeToFile(readingFile('names.txt'))
