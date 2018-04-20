from math import *

n = eval(input('Enter a number '))
times = eval(input('How many iterations '))
for i in range(times):
    newt = 2 / n
    newton = (newt + n) / 2
    n = newton
    print(newton)
