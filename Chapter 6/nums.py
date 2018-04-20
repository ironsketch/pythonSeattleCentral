L = []
def average():
    counter = 0
    fileOpen = open('Grades.txt', 'r')
    for grade in fileOpen:
        L.append(float(grade))
    fileOpen.close()
    for i in L:
        counter += i
    total = counter / (len(L) + 1)
    print (total)

average()
