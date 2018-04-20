# The Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.

# Based on definition provided by Google, I am going to attempt
# this without looking at the HW 2 Solns_1.py
def fib():

    # Assigning Variables
    aNum = 0
    bNum = 1
    cNum = 1

    # Printing first variables
    print(aNum)
    print(bNum)
    print(cNum)

    # Running through Fibonacci sequence 10 times
    # Clunky and stupid. Not nice like the teachers
    # I make each number add the last two that were
    # just added and I run that 10 times
    for i in range (10):
        aNum = bNum + cNum
        print(aNum)
        bNum = aNum + cNum
        print(bNum)
        cNum = aNum + bNum
        print(cNum)

# Calling def fib
fib()
