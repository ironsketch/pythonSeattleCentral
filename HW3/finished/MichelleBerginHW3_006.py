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
