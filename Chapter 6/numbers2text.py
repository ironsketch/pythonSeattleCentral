# numbers2text.py
#     A program to convert a sequence of Unicode numbers into
#         a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")
    
    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)           # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message

    print("\nThe decoded message is:", message)

main()

>>> 
This program converts a sequence of Unicode numbers into
the string of text that it represents.

Please enter the Unicode-encoded message: 102 114 105 101 115 32 116 111 32 103 111 32 

The decoded message is: fries to go 
>>> 
