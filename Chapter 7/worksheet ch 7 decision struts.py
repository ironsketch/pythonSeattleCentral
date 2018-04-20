# convert2.py
#      A program to convert Celsius temps to Fahrenheit.
#      This version issues heat and cold warnings.

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")

main()

## The 2 boolean conditions above are mutually exclusive. (What
## does that mean?)
## Rewrite the program using alternate conditionals.
## Save your program as convert2_alt.py


## Write a function, cond_1(L), that takes a list L which contains
## strings and ints, as a parameter
## and which prints out the even ints, the odd ints, the strings with
## an even number of chars and the strings with an odd number of chars.
## Uses list accumulators and the .append method.  
## Are these mutually exclusive possibilities?
## L = ['one',2,'buckle',3,7,10,'book','python',16,17,'gold','myrh']
## cond_1(L)
## >>> 
## Even ints: [2, 10, 16].
## Odd ints: [3, 7, 17].
## Even numbered strings: ['buckle', 'book', 'python', 'gold', 'myrh'].
## Odd numbered strings: ['one'].


## conditional program execution & importing  functions
##
## If you write a function, then use it as a helper
## function in another new function definition,
## you can of course copy & paste the helper function
## in the same file with the new function.
##
## There is another more versatile method.
## Let's take an example we have already done:
## encodeCharCir(c,n), which encode a single char with
## a circular Caesar cipher with a letter shift of n
## and
## encodeWordCir(word,n), which encodes a word, letter by
## letter, with a circular Caesar cipher, and which uses
## an empty string accumulator to put the encoded letters into.
#
## Originally, (well, with a little extra tweak) we wrote this .....

def encodeCharCir(c,n):
    '''Takes a character, c, and returns the
character that corresponds to the ord of c  plus n.
Wraps around to alphabet start as reqd.  Assumes
c is a lowercase letter.
'''
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    ndx = alfa.find(c)
    new_ndx = (ndx + n) % 26
    new_char = alfa[new_ndx]
    return new_char


    
def main(): ## tests encodeCharCir(c,n)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(c,encodeCharCir(c,3))

main()
## If encodeCharCir.py is run,  main() is run.
## If encodeCharCir.py is imported by another file,
## main() its funcs will be imported but main()
## will be run

##if __name__ == '__main__':
##    main()

*************************************************

## ....... and this was output to the terminal:
>>> 
a d
b e
c f
d g
e h
f i
g j
h k
i l
j m
k n
l o
m p
n q
o r
p s
q t
r u
s v
t w
u x
v y
w z
x a
y b
z c
>>> 

## Then we wrote the next function (with another tweak), encodeWordCir(Word,n)  using the orig function
## & stored it in the file encodeWordCir.py......

def encodeCharCir(c,n):
    '''Takes a character, c, and returns the
character that corresponds to the ord of c  plus n.
Wraps around to alphabet start as reqd.  Assumes
c is a lowercase letter.
'''
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    ndx = alfa.find(c)
    new_ndx = (ndx + n) % 26
    new_char = alfa[new_ndx]
    return new_char

##from encodeCharCir import encodeCharCir ## this is the file name, not the function name
    
def encodeWordCir(word,n):
    '''
Takes a word
## consisting entirely of lowercase letters, and which returns a
## word each letter of which is shifter up by n and which wraps
## to the beginning of the alphabet as reqd.  Use an empty string
## accumulator to build the new word by using encodeCharCir(c,n)
'''
    new_word = '' ## empty string accumulator
    for c in word:
        new_word += encodeCharCir(c,n)
    return new_word

def main():
    for word in ['oz', 'wizard','toto']:
        print('{0} shifted by 5 is {1}'.format(word,encodeWordCir(word,5)))
        print()

main()

## ... the file contained the helper function,  encodeCharCir(c,n),
## the  new function, encodeWordCir(word,n), and a sample run
## encoding each word in a list of words with a circular Caesar cipher
## with a shift of 5:
    
>>> 
oz shifted by 5 is te

wizard shifted by 5 is bnefwi

toto shifted by 5 is ytyt

## Let's comment out the cut & paste of the helper function
## and do this the new way.
*******************************
this is the modified file encodeWordCir.py
We are importing code from the file encodeCharCir.py.
****************************************

##def encodeCharCir(c,n):
##    '''Takes a character, c, and returns the
##character that corresponds to the ord of c  plus n.
##Wraps around to alphabet start as reqd.  Assumes
##c is a lowercase letter.
##'''
##    alfa = 'abcdefghijklmnopqrstuvwxyz'
##    ndx = alfa.find(c)
##    new_ndx = (ndx + n) % 26
##    new_char = alfa[new_ndx]
##    return new_char

from encodeCharCir import encodeCharCir ## this is the file name, not the function name
    
def encodeWordCir(word,n):
    '''
Takes a word
## consisting entirely of lowercase letters, and which returns a
## word each letter of which is shifter up by n and which wraps
## to the beginning of the alphabet as reqd.  Use an empty string
## accumulator to build the new word by using encodeCharCir(c,n)
'''
    new_word = '' ## empty string accumulator
    for c in word:
        new_word += encodeCharCir(c,n)
    return new_word

def main():
    for word in ['oz', 'wizard','toto']:
        print('{0} shifted by 5 is {1}'.format(word,encodeWordCir(word,5)))
        print()

main()


*******************
Note that, as written, the file encodeCharCir.py must be in the same folder
as the file encodeWordCir.py
******************
## The result of running the above file is:
>>> 
a d
b e
c f
d g
e h
f i
g j
h k
i l
j m
k n
l o
m p
n q
o r
p s
q t
r u
s v
t w
u x
v y
w z
x a
y b
z c
oz shifted by 5 is te

wizard shifted by 5 is bnefwi

toto shifted by 5 is ytyt

## We got more than we bargained for - we did indeed import
## the helper function encodeCharCir(Chr,n) from  encodeCharCir.py.
## But we ran the test code at the bottom of encodeCharCir.py.
## We can eliminate this side effect by changing encodeCharCir.py:

***************************
def encodeCharCir(c,n):
    '''Takes a character, c, and returns the
character that corresponds to the ord of c  plus n.
Wraps around to alphabet start as reqd.  Assumes
c is a lowercase letter.
'''
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    ndx = alfa.find(c)
    new_ndx = (ndx + n) % 26
    new_char = alfa[new_ndx]
    return new_char


    
def main(): ## tests encodeCharCir(c,n)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(c,encodeCharCir(c,3))

## main()
## If encodeCharCir.py is run,  all the code in the file
## will be run.
## If encodeCharCir.py is imported by another file,
## encodeCharCir.py will not be run, but its definitions
## will be imported.



if __name__ == '__main__':
    main()

## If encodeCharCir.py is run directly ,  
## main() will be run.
## If encodeCharCir.py is imported by another file,
## main() will not be run, but its definitions
## will be imported.


if __name__ == '__main()__':
    main()

**************************************

## With this mod in encodeCharCir.py, running
## encodeWordCir.py makes encodeCharCir(Chr,n) available
## to encodeWordCir(Word,n) without running the
## test code at the bottom of encodeCharCir.py.
## Running encodeWordCir.py now produces what we want:
***************************************
>>> 
oz shifted by 5 is te

wizard shifted by 5 is bnefwi

toto shifted by 5 is ytyt

>>> 

## Write a function sub2From(x),
## that returns x -2. Include a main()
## that cycles through the list [1,2,8,16]
## and uses sub2From(x) to print out each int in the list
## and the int - 2 on the same line.  Use the conditional
## run main statements at code bottom.
## Save your code in sub2From.py
## Write a function, sub2FromAndSqr(x),
## which returns (x-2)**2 and which uses
## sub2From(x) as a helper function by importing it.
## Include a main() that
## cycles through the list [1,2,8,16]
## and uses sub2FromAndSqr(x) to print out each int in the list
## and the (int - 2)**2 on the same line. 




## Boolean operators: and, or, not
b1 = (2 > 1);    b2 = (3 < 1);     b3 = (5 == 5)
##    True             False              True
not b1
not b2
not b3

b1 and b2
b1 and b3

b1 or b2
b1 or b3

not(b1 and b2)
not(b1 and b3)

not(b1 or b2)
not(b1 or b3)

b1 and not b2
b1 and not b3

b1 or not b2
b1 or not b3

## Rewrite cond_1(L) using boolean operators.  Call the new
## function cond_2(L)

## Write a function, cond_3(L), which take a list L containing
## strings and ints as a parameter and which prints out words
## strings that contain "y", strings of length 4, ints divisible
## by 5 but not divisible by 2, ints greater than 7.
## Use boolean operators.  Are the conditions mutually exclusive?

## L = ['one',2,'buckle',3,7,10,'book','python',16,17,'gold','myrh',15,25,20,30,35]
## cond_3(L)
##
## >>> 
## Strings containing "y": ['python', 'myrh']
## Strings of length 4:    ['book', 'gold', 'myrh']
## Odd Ints div by 5:      [15, 25, 35]
## Ints greater than 7:    [10, 16, 17, 15, 25, 20, 30, 35]

## Write a function, BMI_val(wt,ht), that returns a person's body mass index given
## their weight in lbs and height in inches.  The formula for bmi is:
## bmi = 720 * wt/ht**2.

## Write a function, BMI_assess(wt,ht), that uses bmi(wt,ht) as a helper function
## and which prints out a message "normal",
## if 19 <= bmi <= 25,
## "below normal", if bmi < 19 and "above normal" if bmi > 25.
## Use BMI_assess(wt,ht) to traverse a list of tuples with weight and height &
## print out an appropriate message for each.
## L = [(170,74),(74,170),(250,48),(250,96)]
## >>> 
## Your wt of 170.0 lbs and ht of 74.0 inches give a bmi of 22.4, 
## which is normal.
## Your wt of 74.0 lbs and ht of 170.0 inches give a bmi of  1.8, 
## which is below normal.
## Your wt of 250.0 lbs and ht of 48.0 inches give a bmi of 78.1, 
## which is above normal.
## Your wt of 250.0 lbs and ht of 96.0 inches give a bmi of 19.5, 
## which is normal.
