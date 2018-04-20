def main():
    print("Caesar cipher")
    print()

    key = eval(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")

    
    cipher = ""
    for word in plain.split():
        for letter in word:
            cipher = cipher + chr(ord(letter) + key)
        cipher = cipher + ' '  ## put spaces back

    print("Encoded message follows:")
    print(cipher[:-1])   ## take out last space

    ## to decode, simply use -ve of the key
    decipher = ""
    for word in cipher.split():
        for letter in word:
            decipher = decipher + chr(ord(letter) - key)
        decipher = decipher + ' '  ## put spaces back

    print("Decoded message follows:")
    print(decipher[:-1])   ## take out last space
    
main()
