# c08ex01.py
#    Nth fibonacci number

def main():
    print("This program calculates the nth Fibonacci value.\n")

    n = eval(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr

    print("The nth Fibonacci number is", curr)

if __name__ == '__main__':
    main()
##>>> 
##This program calculates the nth Fibonacci value.
##
##Enter the value of n: 20
##The nth Fibonacci number is 6765
##>>> 


# c08ex02.py
#   Windchill Table

def windChill(t, v):
    if v > 3:
        chill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    else:
        chill = t
    return chill

def main():

    # Print table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(70))
    print("MPH|", end=' ')
    temps = list(range(-20,61,10))
    for t in temps:
        print("{0:5}".format(t), end=' ')
    print("\n---+" + 55 * '-')

    # Print lines in table
    for vel in range(0,51,5):
        print("{0:3}|".format(vel), end=' ')
        for temp in temps:
            print("{0:5.0f}".format(windChill(temp, vel)), end=' ')
        print()
    print()

main()

##main()
##
##Wind Chill Table
##
##
##                             Temperature                              
##MPH|   -20   -10     0    10    20    30    40    50    60 
##---+-------------------------------------------------------
##  0|   -20   -10     0    10    20    30    40    50    60 
##  5|   -34   -22   -11     1    13    25    36    48    60 
## 10|   -41   -28   -16    -4     9    21    34    46    58 
## 15|   -45   -32   -19    -7     6    19    32    45    57 
## 20|   -48   -35   -22    -9     4    17    30    44    57 
## 25|   -51   -37   -24   -11     3    16    29    43    56 
## 30|   -53   -39   -26   -12     1    15    28    42    56 
## 35|   -55   -41   -27   -14     0    14    28    41    55 
## 40|   -57   -43   -29   -15    -1    13    27    41    55 
## 45|   -58   -44   -30   -16    -2    12    26    40    54 
## 50|   -60   -45   -31   -17    -3    12    26    40    54 


#c08ex03.py
#    Years for investment to double

def main():
    print("Number of years for an investment to double.\n")

    apr = eval(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal*(1+apr)
        years = years + 1

    print("Years to double:", years)

if __name__ == '__main__':
    main()
##>>> 
##Number of years for an investment to double.
##
##What is the annual interest rate? .06
##Years to double: 12
##>>> 



# c08ex05.py
#   Primality tester

import math

def isPrime(n):
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True

def main():
    print("Prime number tester\n")
    n = eval(input("Enter a value to test: "))
    if isPrime(n):
        print(n, "is prime.")
    else:
        print(n, "is not prime.")

if __name__ == '__main__':
    main()
##Prime number tester
##
##Enter a value to test: 131
##131 is prime.
##>>> main()
##Prime number tester
##
##Enter a value to test: 311
##311 is prime.
##>>> main()
##Prime number tester
##
##Enter a value to test: 113
##113 is prime.
##>>> 


# c08ex06.py
#    primes to n

from c08ex05 import isPrime

def main():
    print("This program finds all prime numbers up to N\n")
    n = eval(input("Enter the upper limit, n: "))
    print("primes: ", end=' ')
    for i in range(2,n+1):
        if isPrime(i):
            print(i, end=' ')
    print("Done")

if __name__ == '__main__':
    main()
##This program finds all prime numbers up to N
##
##Enter the upper limit, n: 311
##primes:  3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
##67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139
##149 151 157 163 167 173 179 181 191 193 197 199 211 223
##227 229 233 239 241 251 257 263 269 271 277 281 283 293
##307 311 Done
##>>> 

# c08ex07.py
#    Goldbach tester

from c08ex05 import isPrime

def goldbach(x):
    cand = 3
    while cand < x/2:
        other = x - cand
        if isPrime(cand) and isPrime(other):
            return cand
        cand = cand + 2

def main():
    print("Goldbach checker\n")
    
    n = eval(input("Enter an even natural number: "))
    if n % 2 != 0:
        print(n, "is not even!")
    else:
        prime1 = goldbach(n)
        prime2 = n - prime1
        print("{0} + {1} = {2}".format(prime1, prime2, n))

def goldbach1(x):
    '''
Returns a list of all goldbach pairs for x.
'''
    cand = 3
    L = []
    while cand < x/2:
        other = x - cand
        if isPrime(cand) and isPrime(other):
            L1 = [cand,other]
            L1.sort()
            if L1 not in L:
                L.append(L1)
        cand = cand + 2
    return L

##
##if __name__ == '__main__':
##    main()

##>>> goldbach1(200)
##[[3, 197], [7, 193], [19, 181], [37, 163], [43, 157],
##[61, 139], [73, 127], [97, 103]]
##>>> 
    
