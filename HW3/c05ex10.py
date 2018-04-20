# c05ex10.py
#   Average word length


def main():
    '''
Get phrase from user
Create & initialize word counter
Create & initialize letter counter
For each word in message
  increment word counter
  increment letter counter by number of letters in word
Compute avg word length = (total number of letters)/(number of words
'''
    print("Average word length")
    print()

    phrase = input("Enter a phrase: ")

    # using accumulator loop
    wordCount = 0  ## word counter
    letterCount =0 ## letter counter 
    for word in phrase.split():
        letterCount = letterCount + len(word)
        wordCount = wordCount + 1

    print("Average word length", letterCount/wordCount)

main()

#Average word length
#
#Enter a phrase: john zelle is a computer science teacher at a four year college and the author of our book.
#Average word length 4.111111111111111
#>>>