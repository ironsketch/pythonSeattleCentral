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
