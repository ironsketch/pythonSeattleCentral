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
