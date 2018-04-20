# File: c01ex3.py
# substitutes 2.0 for 3.9
'''
Modify the Chaos program using 2.0 in place of 3.9 as the multiplier
in the logistic function.
Your modified line of code should look like this:
x = 2.0 * x * (1 - x)
Run the program for various input values and compare the results
to those obtained from the
original program. Write a short paragraph describing any
differences that you notice in the
behavior of the two versions.
'''
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
main()
##>>> 
##This program illustrates a chaotic function
##Enter a number between 0 and 1: .25
##0.375
##0.46875
##0.498046875
##0.49999237060546875
##0.4999999998835847
##0.5
##0.5
##0.5
##0.5
##0.5
##>>>

# File: c01ex5.py
# Chaos program that prints a variable number of terms
'''
Modify the Chaos program so that the number of values to
print is determined by the user.
You will have to add a line near the top of the program
to get another value from the user:
n = eval(input("How many numbers should I print? "))
Then you will need to change the loop to use n instead of a specific number.
'''
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
main()
##>>> 
##This program illustrates a chaotic function
##Enter a number between 0 and 1: .25
##How many numbers should I print? 7
##0.73125
##0.76644140625
##0.6981350104385375
##0.8218958187902304
##0.5708940191969317
##0.9553987483642099
##0.166186721954413
##>>> 

# c02ex02.py
# Average 3 exam scores
'''
Modify the avg2.py program (Section 2.5.3) to find the average
of three exam scores.
'''
def main():
    print("This program computes the average of three exam scores.")
    print()
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3.0
    print("The average of the scores is:", average)
main()
##>>> 
##This program computes the average of three exam scores.
##
##Enter three scores separated by a comma: 70,75,80
##The average of the scores is: 75.0
##>>> 

# c02ex03.py
#   Loop to perform 5 temperature conversions
'''
Modify the convert.py program (Section 2.2) with a loop
so that it executes 5 times before
quitting (i.e., it converts 5 temperatures in a row).
'''
def main():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()
main()
##>>> 
##What is the Celsius temperature? 100
##The temperature is 212.0 degrees Fahrenheit.
##
##What is the Celsius temperature? 0
##The temperature is 32.0 degrees Fahrenheit.
##
##What is the Celsius temperature? 20
##The temperature is 68.0 degrees Fahrenheit.
##
##What is the Celsius temperature? 40
##The temperature is 104.0 degrees Fahrenheit.
##
##What is the Celsius temperature? 60
##The temperature is 140.0 degrees Fahrenheit.
##
##>>> 

# c02ex06.py
#    Future value of amount invested yearly
'''
Suppose you have an investment plan where you invest a certain
fixed amount every year.
Modify futval.py to compute the total accumulation of
your investment. The inputs to the
program will be the amount to invest each year, the interest rate,
and the number of years for
the investment.
'''
def main():
    print("This program calculates the future value of a yearly investment")
    print()
    payment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))
    principal = 0.0
    for i in range(years):
        principal = (principal + payment) * (1 + apr)
    print("The amount in", years, "years is:", principal)
main()
##>>> 
##This program calculates the future value of a yearly investment
##
##Enter amount to invest each year: 250
##Enter the annualized interest rate: 0.05
##Enter the number of years: 20
##The amount in 20 years is: 8679.812952008211
##>>> 

