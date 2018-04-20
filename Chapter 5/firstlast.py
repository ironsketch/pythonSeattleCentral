L = [('Mother', 'Fucker'), ('Barry', 'Bob'), ('Moby', 'BIGDick'), ('HARBLEGARBLE', 'BLEECCHHHHHH')]

def userName(first,last):
    user = first[0] + last [:7]
    user = user.lower()
    return user

def printOut(L):
    for i in L:
        print(i[0],i[1], ' has the username of ', userName(i[0],i[1]))

printOut(L)
