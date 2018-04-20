#05
################################################
##                  Zelle 8.5                 ##
################################################
from math import *

def isPrime(n):
    L = []
    sqrtN = int(sqrt(n))
    a = 0
    for i in range(2,sqrtN):
        while a != 0:
            a = n % i
            L.append(a)

    total = 0
    for item in L:
        total += item

    TV = total == 0
    return TV
n = 8
print('It is,',isPrime(n),'that,',n,'is a prime number.')
