# The main function of the program
def main ():
    
    print('Calcuclate your yearly investment!')
    print()

    # Getting 3 inputs from the user and assigning each to a variable
    payment = eval(input('Enter your investment each year: '))
    intrate = eval(input('Enter your interest rate: '))
    years = eval(input('Enter the years that have or will pass: '))

    # Initializing the variable principal at 0.0
    principal = 0.0

    # For loop to calculate the principal based on user input
    for i in range(years):
        principal = (principal + payment) * (1 + intrate)
        
    # Print out of completion of the for loop
    # %.2f % prinicipal truncates the float to 2 decimal places
    print('In ', years, " years you'll have: %.2f" % principal)

main()
