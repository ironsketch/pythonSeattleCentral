# Zelle Ch 1 examples

print('Hello World!')
print(2+3)
print('2 + 3 =',2+3)



def hello():
    print('Hello')
    print('Computers are fun!')

def greet(person):
    '''Simple function with 1 parameter.'''
    print("Hello", person)
    print("How are you?")

greet('John')
greet("Emily")

greet
greet()

# write a function aGreetsb(a,b), which has a introduce
# themselves to b & b introduce themselves to a.

# for loop and range statement
for i in range(5):
    print(i)

# Write a for loop & a range statement that prints out numbers from 0 to 7.

# Write a for loop & a range statement that prints out numbers from 1 to 5.
    

def main():
    # File: chaos.py
    # A simple program illustrating chaotic behavior.
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

main()

