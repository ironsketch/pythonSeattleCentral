'''Use the functions from the previous three problems to implement
a program that computes the sum of the squares of numbers read from
a file. Your program should prompt for a file name and print out the
sum of the squares of the values in the file. Hint: use readlines()'''

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
