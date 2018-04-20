## counting from 1 to 10 with a for loop
for count in range(1,11):
    print(count)

## counting from 1 to 10 with a while loop
count = 0
while count <= 10:
    print(count)
    count += 1

## but, the programmer has more responsibility with a while loop:

x = 0
while x < = 10:
    print(x)


while y <= 10:
    print(y)
    y += 1

while z <= 10:
    print(z)
## 1.0
## There is always a boolean that comes after the while.
## If the boolean if True, statements inside the while execute,
## OTW
## statements inside the while are not executed any more.

## 2.0
## All the variables in the boolean need to be defined.

## 3.0
## Unless variables in the boolean after the while change,
## the loop will go on forever.  So, variables inside the while
## loop need to be updated to eventually make the boolean False
## and thus bring a close to the while loop.

## sentinel loop to get data from the user.  Data termination signaled
## with an Enter without any data.

# average4.py

def main():
    '''
Gets one number at a time from the user and sums
all the numbers entered.  User signals end of data
entry by hitting Enter w/o any other entry.
'''
    Sum = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        Sum = Sum + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit) >> ")
    print("\nThe average of the numbers is", Sum / count)

main()

## using a for loop to read numbers from a file and computing the avg

# average5.py

def main():
    '''
using a for loop to read numbers from
a file and computing the avg.
'''
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    Sum = 0.0
    count = 0
    for line in infile:
        Sum = Sum + eval(line)
        count = count + 1
    infile.close()
    print("\nThe average of the numbers is", Sum / count)

main()

# average6.py

def main():
    '''
Uses a while loop to read numbers from a file
and computes the avg.
'''
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    Sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        Sum = Sum + eval(line)
        count = count + 1
        line = infile.readline()
    infile.close()
    print("\nThe average of the numbers is", Sum / count)

main()

##
## Write a function, guessNum(), which uses a while loop, in which the computer
## chooses a secret number between 1 and 128
## and the user makes multiple guesses of the secret number.
## For each guess, the computer tells the user if the guess
## is too low or too high.  User's score starts at 100 and decreases
## by 2 for each incorrect guess.  When the secret number if finally guessed,
## a nicely formatted printout is made with the final score, the secret number
## and the guesses made.  If the secret number is guessed on the 1st try, a
## congratulatory message is also made.

>>> 
Welcome to the number guessing game.
Guess a natural number between
1 and 128. Score starts at 100 and
decreases by 2 for every guess.
Game is over when user guesses secret number.
What's your guess? 64
Your guess is too low.
What's your guess? 96
Your guess is too low.
What's your guess? 122
Your guess is too high.
What's your guess? 114
Your guess is too low.
What's your guess? 105
Your guess is too low.
What's your guess? 109
Your guess is too low.
What's your guess? 112
Your guess is too low.
What's your guess? 113
Your guess is too low.
What's your guess? 118
Your guess is too low.
What's your guess? 120
Your guess is too high.
What's your guess? 119
Your score is 80.
Secret number is 119.
Your guesses were:  [64, 96, 122, 114, 105, 109, 112, 113, 118, 120, 119]
>>> 

## nested loops
def nestedLoop():
    for outer in ['aa','yy','zz']:
        for inner in ['mmm','ooo']:
            print(outer, inner)

nestedLoop()
##>>> 
##aa mmm
##aa ooo
##yy mmm
##yy ooo
##zz mmm
##zz ooo

## Write a function NL_1(), which uses a nested for loop to print out:
>>> 
I went.
I ran.
I said.
You went.
You ran.
You said.
He went.
He ran.
He said.
She went.
She ran.
She said.
>>> 
## Write a function LoopInLoopInLoop(L1,L2,L3),
## with appropriate values for L1,L2,L3, which prints out:

>>> 
Jon runs to work.
Jon runs from home.
Jon runs all the time.
Jon walks to work.
Jon walks from home.
Jon walks all the time.
Jon rides to work.
Jon rides from home.
Jon rides all the time.
Jill runs to work.
Jill runs from home.
Jill runs all the time.
Jill walks to work.
Jill walks from home.
Jill walks all the time.
Jill rides to work.
Jill rides from home.
Jill rides all the time.
Jay runs to work.
Jay runs from home.
Jay runs all the time.
Jay walks to work.
Jay walks from home.
Jay walks all the time.
Jay rides to work.
Jay rides from home.
Jay rides all the time.
## Morgan's Laws
## Make truth tables to confirm that
## not (a  or b )   is the same as   (not a ) and (not b)
## not (a and b )   is the same as   (not a )  or (not b)

## boolean algebra
a and False == False
a and True  == a
a  or False == a
a or True   == True
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)
not(not a) == a



## Using python to print out a truth table:

def TrthPAndQ():
    """Generates truth table for and."""
    print("{:^7}   {:^7}  {:^7}".format("P", "Q ", "P and Q"))
    print("-"*30)
##             P         Q        P and Q
##    print("  {0}    {1}     {2}  ".format(b1,b2,b1 and b2)
    for P in [True,False]:
        for Q in [True,False]:
            print("{:^7}   {:^7}  {:^7}".format(str(P),str(Q),str(P and Q)))
            ## print("{:^7}   {:^7}  {:^7}".format(P,Q,P and Q))


            ## need str() to print out True or False instead of 1 or 0

## Write the following function.
## WCheck your output by hand.
## WHow many rows with the table have?
## WHow many nested loops do you need?
## WSample run:

>>> 
   P     Q       R      S   (P and Q) or (R and S)
--------------------------------------------------
 True   True   True   True          True        
 True   True   True   False         True        
 True   True   False  True          True        
 True   True   False  False         True        
 True   False  True   True          True        
 True   False  True   False        False        
 True   False  False  True         False        
 True   False  False  False        False        
 False  True   True   True          True        
 False  True   True   False        False        
 False  True   False  True         False        
 False  True   False  False        False        
 False  False  True   True          True        
 False  False  True   False        False        
 False  False  False  True         False        
 False  False  False  False        False        
>>>     

## Some pitfalls
while (a  == 5  or a == 7):
is not equivalent to
while (a  == 5 or 7):
## Any built in type can be interpreted as a boolean.
##    ints and floats:  a zero is interpreted as False, non zero as True
bool(0)
bool(0.0)
bool(5.0)
bool(-1)
##  sequences are interpreted as False if empty, as True if not empty
x and y   returns x if x is False;   returns  y if x is True
x or y    returns x if x is  True;   returns y  if x is False

## This means that

a  == 5 or 7

## will always evaluate as True
(a  == 5) or 7
Since 7, interpreted as a boolean, is True, the whole boolean will be True.

# Use isPrime(n) and isFactor(f,n) to write a function primeFactorsOf(n),
# which returns a list of the prime factors of an integer n >0.
# 
# Use primeFactorsOf(n) write a function
# to print out a a nicely formated table of ints
# from 2 to 20 with their prime factors.
# Then generalize the last exercise by writing a function, primeTable(a,b),
# which prints a out a table of primes in the specified range, including a and b.
print(8,primeFactorsOf(8))
print(9,primeFactorsOf(9))
print(10,primeFactorsOf(10))
print(11,primeFactorsOf(11))
print(12,primeFactorsOf(12))

>>>
8 [2, 2, 2]
9 [3, 3]
10 [2, 5]
11 [11]
12 [2, 2, 3]

primeTable(900,920)

     Number          Prime Factors
 ----------   --------------------
        900     [2, 2, 3, 3, 5, 5]
        901               [17, 53]
        902            [2, 11, 41]
        903             [3, 7, 43]
        904         [2, 2, 2, 113]
        905               [5, 181]
        906            [2, 3, 151]
        907                  [907]
        908            [2, 2, 227]
        909            [3, 3, 101]
        910          [2, 5, 7, 13]
        911                  [911]
        912    [2, 2, 2, 2, 3, 19]
        913               [11, 83]
        914               [2, 457]
        915             [3, 5, 61]
        916            [2, 2, 229]
        917               [7, 131]
        918       [2, 3, 3, 3, 17]
        919                  [919]
        920       [2, 2, 2, 5, 23]
