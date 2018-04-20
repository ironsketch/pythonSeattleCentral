import math  # Makes the math library available.

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    d = (b * b - 4 * a * c)
    def quad(a,b,c):
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        return root1, root2
    if d > 0:
        print()
        print("The solutions are: ", quad(a,b,c))
    elif d == 0:
        print()
        quad(a,b,c)
        print("The solution is: ", quad(a,b,c) )
    else:
        print("You have no real roots...")

    

main()
