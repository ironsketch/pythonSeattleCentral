# c05ex03.py
#    Exam grader

def main():
    '''
Produce a string of grade letters
using string repetition
so that an integer grade from 0 to 100
can be used as an index into the string.

This is more straightforward with if...elif.
'''
    print("Exam Grader")
    score = eval(input("Enter the score (out of 100): "))
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print("The grade is", grades[score])

main()

#Exam Grader
#Enter the score (out of 100): 72
#The grade is C
#>>> main()
#Exam Grader
#Enter the score (out of 100): 81
#The grade is B
#>>> main()
#Exam Grader
#Enter the score (out of 100): 93
#The grade is A
#>>> main()
#Exam Grader
#Enter the score (out of 100): 22
#The grade is F
#>>> main()
#Exam Grader
#Enter the score (out of 100): 65
#The grade is D
#>>> 
