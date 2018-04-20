# c05ex14.py
#Program to count lines,words,characters in a file.
def main():
    '''
get filename from user
open file for reading
read in whole file, assign to chars
close file
# characters in chars = len(chars)
# words in chars = len(chars.split())
# lines in chars = len(chars.split('/n'))
'''
    print("File wordcount")
    print()

    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    chars = infile.read() ## all chars read from file
    infile.close()
    
    words = chars.split()  ## words put into a list
    lines = chars.split("\n") ## lines put into a list
##
    print(chars)
    print(words)
    print(lines)
    print('Print out character #, character: ')
    n = 0
    for char in chars:
        n += 1
        print(n,char)

    ## number of characters = len(chars)
    print("Characters:", len(chars))
    ## number of words = len of list of words
    print("Words:", len(words))   
    ## number of lines = len of list of lines
    print("Lines:", len(lines))

main()

