## List is mutable
## Tuple is NOT
##
##FRACK = ['FRKJOO', 'ETHHERL']
##FRACK2 = ['FRKJOO','ETHHERL']
##sto = 'ewanfibsflnsoijn;oajnsda  ak vdlkjvas djkf asjlkdf  '
##
##print(FRACK[1].upper())
##print(FRACK2[1].upper())
##print(FRACK[0].find('JOO'))
##print(sto.count('a'))
##print(sto.replace('a',' FUCK YOU '))
##POOP = sto.split()
##print(POOP)
##stop = ' '.join(POOP)
##print(stop)


##def userName(first,last):
##    lastLen = len(last)
##    remainder = 7 % lastLen
##    username = first[:1] + last[remainder - 2:lastLen + 1]
##    username = username.lower()
##    return username
##
##print(userName('Michelle','poo'))

L = ('Mother Fucker', 'Barry Bob', 'Moby BIGDick', 'HARBLEGARBLE BLEECCHHHHHH')

def userName(firstlast):
    split = firstlast.split()
    first = split[0]
    last = split[1]
    user = first[0] + last [:7]
    return user

def printOut(L):
    for i in L:
        print(i, ' has the username of ', userName(i))

printOut(L)
