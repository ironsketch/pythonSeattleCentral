def main():
    print('Find your exam grade')

    # Collecting grade from user
    score = eval(input('Enter your grade out of 100: '))

    # Basically an if elif statement because from what I can
    # understand, the variable grade is holding the letter
    # F, 60 times and D 10 times and C 20 etc. to 11 times A
    
    grade = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"

    # Then the [] is looking for the location based on the number
    # entered by the user to find the spot in the string where
    # the letter lies. So it is creating an if elif statement
    # but with less programming .... i think ....
    print('Your grade be',grade[score])

main()
