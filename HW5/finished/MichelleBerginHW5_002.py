'''A certain CS professor gives 100-point exams that are graded
on the scale 90–100:A, 80–89:B, 70–79:C, 60–69:D, <60:F. Write
a program that accepts an exam score as input and uses a decision
structure to calculate the corresponding grade.'''

#02
################################################
##          Zelle 7.3 – compute grade         ##
################################################

def score(grade):

    # If else statements. Each uses a boolean to
    # find if it is true or not
    # Python works from top to bottom for these
    # that I made. first it will check if it is an A
    # If I had put B before A it would always be true if
    # any grade is above 80. Thus never returning an A
    # That is why it is in this order
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

for i in range(0,101,10):
    print(score(i),i)
