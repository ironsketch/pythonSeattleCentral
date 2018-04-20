from string import ascii_lowercase

def enc(char,shift):
    if char not in ascii_lowercase:
        return char
    else:
        ndx = ascii_lowercase.find(char)
        newNdx = (ndx + shift) % 26
        return ascii_lowercase[newNdx]

def en(plainTxt,shift):
    code = ''
    for char in plainTxt:
        code += enc(char,shift)
    return code

def main():

    plainTxt = input('Enter something to cipher ')
    print(en(plainTxt,4))

main()
