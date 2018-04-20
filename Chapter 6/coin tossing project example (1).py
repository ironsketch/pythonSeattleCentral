##1. Use CT_qTosses_zTimes(q,z,pH) with q = 10, z = 10000, pH = 0.6
##to create a dictionary with keys from 0 to 10 representing the number
##of heads and with values equal to the number of times that number of heads
##was obtained in 10000 10-tosses.
##2.  Use ProbHead(nTosses,n_H,p_H) with nTosses = 10, and p_h = 0.6 to create
##a 2nd dictionary with keys from 0 to 10 representing the number
##of heads and with values equal to the probability of getting that number of
##heads.
##3. Convert the 1st dictionary to a probability dictionary by dividing all the
##values by 10000 to get an experimental probability.
##4. print out a nicely formatted table with the following columns:
### heads    # tails   sim prob     pred prob     sim prob - pred prob
##
##5. same as 4 but print to file


from random import random

def CT(pH):
    '''
Flips a coin once, returning 1 for H
0 for T.  H have a prob of pH.
If pH = 0.5, coin is fair.
'''
    flip = random() ## float between 0 and 1
    if flip < pH:
        return 1
    else:
        return 0   
    
def CT_qToss(q,pH):
    '''
tosses a coin
# q times & which returns the number of Heads.
# Uses CT(pH).  pH is the probability of getting a Head.
'''
    numHeads = 0  ## counts head tossed
    for flips in range(q): ## flip the coin q times
        coinFlipResult = CT(pH)
        numHeads += coinFlipResult
    return numHeads
        
def CT_qTosses_zTimes(q,z,pH):
    '''
# Repeats a qToss z times.  Returns a dictionary
# with keys = nH for each qToss and values = # times that
# nH occurred.  Note that 0 <= nH <= q.
'''
    d = dict()  ## accum for results
    for i in range(q+1): ## zero out dict before starting to flip
        d[i] = 0
    for i in range(z):  ## repeat z times
        resultOfqToss = CT_qToss(q,pH)
        d[resultOfqToss] += 1
    return d   


def factorial(n):
    acum = 1
    for i in range(1,n+1):
        acum *= i
    return acum


def Cnm(n,m):
    '''n!/(m!(n-m)!)
'''
    num = factorial(n)
    denom1 = factorial(m)
    denom2 = factorial(n-m)
    denom = denom1 * denom2
    return num/denom

def ProbHead(nTosses,n_H,p_H):
    '''
Probability of n_H Heads if n tosses are made
with a coin having probality of head = p_H.
'''
    p_T = 1 - p_H
    n_T = nTosses-n_H
    val = Cnm(nTosses,n_H)*(p_H**n_H)*(p_T**n_T)
    return val




    
    
