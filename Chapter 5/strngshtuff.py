##def poop(s,n):
##    for ndx in range(len(s)-(n-1)):
##        print(s[ndx:ndx+1])
##
##for n in range (1,9):
##    poop('FUCKERMOTHERFUCK',n)
##    print('-----------')


def down(word):
    n = len(word)
    for i in range(n):
        print (word[:n])
        n -= 1
        
def up(word):
    n = len(word)
    for i in range(n):
        print (word[:i])

def upDown(word):
    up(word)
    down(word)
        
upDown('ILOVECATS<3')
        
##def upDown(word):
##    acum = ''
##    n = len(word)
##    print(n)
####    for i in range (n):
####        for c in word:
####            print (acum)
####            acum += c
####        
##
##upDown('FUCKERMOTHERFUCK')
