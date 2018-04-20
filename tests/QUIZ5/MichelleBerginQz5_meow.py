def appending(doc):
    doc = doc.split('\n')
    for row in doc:
        print (row)

def max_min_Avg(fname):
    inFile = open(fname, 'r')
    docData = inFile.read()
    inFile.close()
    appending(docData)
    for row in docData:
        print(row)

max_min_Avg('quiz5Floats.txt')
