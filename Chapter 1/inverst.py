def main():
    prin = eval(input('Enter in your principle: '))
    intrate = eval(input('Enter your interest rate: '))
    intrate /= 100

    for i in range (10):
        prin *= (1 + intrate)
    print(' in 10 years you\'ll have: %.2f' % prin)

main()
