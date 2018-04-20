# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

# NAMES

# EXPRESSIONS

number = 32
number
text = 'Hello'
text

# OUTPUT STATEMENTS
x = 5
x
print(x)
print(text)
print(Text)


print(3+4)
print(3,4,3+4)
print()
print('The answer is', 3+4)

# ASSIGNMENT STATEMENT
x = 0.2
x = 3.9*x*(1-x)
print(x)

myVar = 0
myVar

myVar = 7
myVar

myVar = myVar + 1
myVar

# sum accumulator
sumAcum = 0
sumAcum = sumAcum + 2
sumAcum = sumAcum + 4
sumAcum = sumAcum + 6
sumAcum

# Write a function,sumAcum_1(), that uses a sum accumulator, a for loop and a range
# statement to find the sum of the first 5 natural numbers.

# ASSIGNING INPUT
name = input('Enter your name: ')
print('Hello',name,'how are your?')

# Example of a function of a function
number = eval(input('Enter a number: '))
print(number,'squared is',number**2)

expr = eval(input('Enter an expression: '))
print(expr)

# Write a function,getAndEvalExpr_1(), that asks the user for an expression,
# then prints out the expression, and the evaluation of the expression.
# If expr = '3+4*2', will print out
# '3 + 4*2 ' is 11
# 

# MULTIPLE ASSIGNMENT

# avg2.py
#   A simple program to average two exam scores  
#   Illustrates use of multiple input

def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)

## Write a function, sumAndProd_1(), which gets 2 numbers from the user
## & prints out the sum and the product of the 2 numbers.


# DEFINITE LOOPS
for i in [0,1,2,3]:
    print(i)

for x in range(3):
    print(x)

for w in range(1,6):
    print(w)

for b in range(2,12,2):
    print(b)

# Write a function, forLoopAndRangeEx_1(),
# that prints out the even numbers
# from 20 to 30 inclusive.Use a for
# loop and a range statement.

# Write a function, forLoopAndRangeEx_2(),
# that prints out the odd numbers
# from 20 to 30 inclusive.Use a for loop
and a range statement.

# Write a function, sumConsecInts(a,b),
# that sums all consecutive ints from
# a to b inclusive.

# FUTURE VALUE

# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
   
    for i in range(10):
        principal = principal * (1 + apr)
        
    print("The value in 10 years is ${0:4.2f}".format(principal))

main()

##>>> 
##This program calculates the future value
##of a 10-year investment.
##Enter the initial principal: 1000
##Enter the annual interest rate: .05
##The value in 10 years is $1628.89
##>>> 
    
# Write a function, C2F_1(), that gets Celsius degrees from the user and prints
# out the equivalent temperature in Fahrenheit degrees.


# Write a function, C2FTable_1():, that prints out a table whose 1st column is Celsius degrees
# from 0 to 90 in steps of 5 and whose second column is the equivalent Fahrenhiet degrees.
# Plan on using a for loop and a range statement.  Incorporate column heading.
