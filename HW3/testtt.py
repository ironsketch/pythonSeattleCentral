L = ['one two three', 'four five six', 'seven eight']
words = ''
poop = str(L)
for word in L:
    poop = word.split(' ')
    str(poop)
    words += poop
    print (poop)
print (words)
