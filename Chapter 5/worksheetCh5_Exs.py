#   'duck'
#    0123

s = 'duck'
s[0]
s[1]
s[2]
s[3]
s[4]

#   '13 ducks'
#    01234567
s1 = ['13 ducks']
#  '13 ducks'
#   01234---
s1[0:5]

len('duck')

# 0 to 1
s[:2]

# 2 to end
s[2:]

# concatenation

x = 'alpha'
y = 'bet'

together = x + y

# repetition
h = 'Hello?'
repeat = 5*h

s[-1]
s[-2]

# last 2 characters
s[-2:]

s[-3:-1]

L = ['Bob','Jill','Jay','Hannah','June']
L[0]
L[1]
L[2]
L[3]
L[5]

len(L)

# Write a function, oneChrPerLine(s), that takes a string, s,
# and prints one character of the string per line.
# Sample runs:
#r
#h
#i
#n
#o
#--------------------
#o
#n
#e
# 
#t
#a
#p

# Write a function, twoChrPerLine(s), that takes a string, s,  NAME:
# and prints two consec character of the string per line.
# Sample runs:
# >>> twoChrPerLine('rhino')
# rh
# hi
# in
# no
# >>> twoChrPerLine('one tap')
# on
# ne
# e
#  t
# ta
# ap

# Write a function, nChrPerLine(s,n), that takes a string, s
# and prints n consec character of the string per line.
# Sample runs:
# >>> nChrPerLine('rhino',2)
# rh
# hi
# in
# no
# >>> nChrPerLine('rhino',3)
# rhi
# hin
# ino
# >>> nChrPerLine('rhino',5)
# rhino
# >>> nChrPerLine('rhino',6)

# Use nChrPerLine(s) to write a function one_nChrperLine(s), 
# which prints out 1  character per line of s, 2 characters 
# per line of s, all the way up to all characters on 1 in.  
# Uses the len(s) BIF from Python.
# Sample run
#h
#e
#n
#r
#y
#
#he
#en
#nr
#ry
#
#hen
#enr
#nry
#
#henr
#enry
#
#henry


# Write a function, backwards(s), that takes a string, s,   
# and prints the string
# backwards.  Use indices.  Sample run:
# >>> backwards('pots')
# stop
    '''
Write a function, updown(s), of length n, that prints
the first 1 chars
the first 2 chars
...
the first n-1 chara
all n chars
the first n-2 chars
...
the first 2 chars
the first 1 chas
Sample Run:
updown('dog')
d
do
dog
do
d
'''

## tuples
T = ('Henry Logan','206-584-1234')
T[0]
T[1]

## string methods (p 140 Zelle)
s = 'Abraham Lincoln'
print(s.lower())
print(s.upper())
print(s.title())
print(s.split())
print(s.find('br'))

s2 = 'here is a longer example'

print(s2.count('er'))
print(s2.find('er'))
print(s2.replace('longer','another'))

L = s.split()
print(L)
s3 = ''.join(L)
print(s3)
s4 = ' '.join(L)
print(s4)

## Write a function, username(first,last), which returns a username
## consisting of the first letter of the first name and (up to) the l
## last 7 letters of the last name. Use the appropriate string method
## to make all the user name characters lower case.[Zelle p 140]
## Sample run:
## print(username('Elizabeth','Taylor'))
## etaylor

## Use username(s) to traverse a list of tuples, each of which
## contains a first and last name, and prints out the first and last
## name with the user name.  You will need to index the members of the
## tuple.
## Sample run:
##('Elmer', 'Fudd') has a username of efudd
##('Donald', 'Duck') has a username of dduck
##('Mickey', 'Mouse') has a username of mmouse


# Write a function, monthNum2Name(num), which returns the full name 
# of a month given the month number, where 1 ~ January, 2 ~ February, etc.
# Do this by putting a list of month names in a list inside the function
# and then using indicies.  Sample run is below. Use the function to print
# out the names of the months corresponding to num = [2,4,5,6,10].  Then use
# the function to print out the month names in reverse order.
# >>> monthNum2Name(4)
# 'April'

## string rep - ord and chr

for lwr in 'abdcefghijklmnopqrstuvwxyz':
    upr = lwr.upper()
    print('{0:3} {1:3}     {2:3} {3:3}'.format(lwr,ord(lwr),upr,ord(upr)))

chr(ord('a'))

ord(chr(97))

# this is an improved 2nd version for zelle ex 5.7

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


## write a function, encodeChar(c,n), which takes a character,c, and returns the
## character that corresponds to the ord of c  plus n.


## Use encodeChar(c,n) to traverse the alphabet and print each letter out
## and the letter shifted up by 3.

## Write a function, encodeCharCir(c,n), which does the same thing as
## encodeChar(c,n) except that letters at the end of the alphabet will
## wrap around to the bgeinning of the alphabet.  Assume all characters
## are lower case letters.

## Use encodeCharCir(c,n) to traverse the alphabet and print each letter out
## and the letter shifted up by 3.


## Write a function, encodeWordCir(word,n), which takes a word
## consisting entirely of lowercase letters, and which returns a
## word each letter of which is shifter up by n and which wraps
## to the beginning of the alphabet as reqd.  Use an empty string
## accumulator to build the new word by using encodeCharCir(c,n).

## use encodeWordCir(word,n) to traverse a list of words and print out
## the original word and the word shifted by 5.


## string formatting
print('{0} has just won ${1:7.2f} in the lottery.'.format('Mr. Smith',12756.67))

def table_Ex1():
    print('{0:^10}  {1:^10}'.format('column 1','column 2'))
    for i in range(200,301,10):
        print('{0:^10}  {1:^10}'.format(i,2*i))
    
## Use string formatting to  write a function, F2CK_table(), that
## prints out a nicely formatted table
## with the 1st colum Faherenheit from 0 to 200 in steps of 10
## the 2nd column the equivalent Celsius temperature,
## & the 3rd column the equivalent temperature in Kelvin 

##>>> 
##    Fahrenheit    Celsius    Kelvin 
##    ----------    -------    ------ 
##        0.00      -17.78     255.37
##       20.00       -6.67     266.48
##       40.00        4.44     277.59
##       60.00       15.56     288.71
##       80.00       26.67     299.82
##      100.00       37.78     310.93
##      120.00       48.89     322.04
##      140.00       60.00     333.15
##      160.00       71.11     344.26
##      180.00       82.22     355.37
##      200.00       93.33     366.48
##>>>     

## opening a file
fin1 = open('nums.txt','r')
fin2 = open('names.txt','r')

## double spacing
fin1 = open('nums.txt','r')
for line in fin1:
    print(line)
fin1.close()

## single spacing, leave off last char of each line, which is '\n'
fin1 = open('nums.txt','r')
for line in fin1:
    print(line[:-1])
fin1.close()

for line in fin2:
    print(line[:-1])
fin2.close()

## writing a file

def fileWriteEx1():
    fout1 = open('F2C.txt','w') # opens file for writing
    for C in range(0,110,10):
        F = 5/9*C  + 32
        print('{0:5.2f},{1:5.2f}'.format(F,C),file = fout1)
    fout1.close()


## appending to a list
L = []
L.append(5)
L.append(7)
L.append(10)
         

## Write a function,sumNumsInFile(fname),
## that opens a file "nums.txt", that contains the
## then floats, one per line,
## 1.25,3.75,2.5,1.75,5.37,2.54
## and which reads the file, adds up the floats & prints out:
## "The sum of the numbers [1.25,3.75,2.5,1.75,5.37,2.54] is 17.16."
## You can create a file of numbers with Notepad or you can use the
## Python editor and save the file as "nums.txt'








	
