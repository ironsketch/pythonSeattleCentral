#YouTube https://youtu.be/OJMoQumklwg
################################################
##                  You Tube                  ##
################################################

def dec2letter(decGrade):

    # if else statment with booleans to decide grade
    if decGrade > 0.92:
        return 'A'
    elif decGrade > 0.85 and decGrade <= 0.92:
        return 'B'
    elif decGrade > 0.78 and decGrade <= 0.85:
        return 'C'
    elif decGrade > 0.65 and decGrade <= 0.78:
        return 'D'
    else:
        return 'E'

def testScores2Letter(fileName):
    L = []
    # Opening file to read it
    fileOpen = open(fileName, 'r')
    for grade in fileOpen:
        # Replacing unwanted characters
        grade = grade.replace('\n','')
        grade = grade.replace(' ','')
        #Splitting it
        grade = grade.split(',')
        # Appending it to list
        L.append(grade)
    # Closing the file
    fileOpen.close()

    #Returning list
    return L

def main():
    #List that was returned
    L = testScores2Letter('decGrades.txt')
    print('{:>10} {:>10} {:>10}'.format('Name','Grade','Average'))
    print('-'*40)
    for item in L:

        #Getting average
        average = float(item[1]) + float(item[2]) + float(item[3]) + float(item[4])
        average /= 4

        #Printing it out nicely
        print('{:>10} {:>10} {:>10.2f}'.format(item[0],dec2letter(average),average))
        
    
main()
