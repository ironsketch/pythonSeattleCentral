#05
################################################
##                  Zelle 8.6                 ##
################################################
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

def main (n):
    for i in range (n):
        if isPrime(i):
            print(i, "is a prime.")
main(14)
