# grades2avg.py
#    Program to find avg and # of grades

def main():
    print("This program finds the average grade and the # of grades.")

    # get the file names
    infileGrades = input("What file are the grades in? ")

    # open the files
    infile = open(infileGrades, "r")

    # process each line of the input file
    counter = 0
    accumulator = 0
    for line in infile:
        accumulator = accumulator + float(line)
        counter = counter + 1


    # close both files
    infile.close()

    print("Grade average is {0:3.3}".format(accumulator/counter))
    print("The number of grades is ",counter)

main()
