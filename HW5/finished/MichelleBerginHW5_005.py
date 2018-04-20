'''A person is eligible to be a US senator if they are at least 30 years
old and have been a US citizen for at least 9 years. To be a US
representative these numbers are 25 and 7, respectively. Write a program
that accepts a person’s age and years of citizenship as input and outputs
their eligibility for the Senate and House.'''

#05
################################################
##       Zelle 7.8 – finds eligibility        ##
################################################

def senate(age,cit):

    # Using a boolean to find out if criteria is met and returning a print
    # string
    if (age >= 30) and cit >= 9:
        eligable = print('You are eligable to be a US senator!')
        return eligable
    else:
        eligable = print('You are NOT eligable to be a US senator...')
        return eligable

def house(age,cit):
    # Using a boolean to find out if criteria is met and returning a print
    # string
    if (age >= 25) and cit >= 7:
        eligable = print('You are eligable to be a US rep')
        return eligable
    else:
        eligable = print('You are NOT eligable to be a US rep')
        return eligable

def main(age,cit):
    senate(age,cit)
    house(age,cit)
    
    
main(25,9)
