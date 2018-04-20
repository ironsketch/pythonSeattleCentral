## YouTube Addy: https://youtu.be/836kybgGyoM

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
