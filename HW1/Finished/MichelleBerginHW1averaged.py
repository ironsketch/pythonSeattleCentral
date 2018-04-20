# The main function of the program
def main():
    print ('Find your average score!')
    print ()

    # Asking user for 3 inputs and consecutively assigning them to
    # the 3 variables to the left
    s1, s2, s3 = eval(input("Enter 3 scores separated by commas: "))

    # The math to find an average of 3 numbers
    a = (s1 + s2 + s3) / 3

    # Printed answer with truncation of the float
    print ("Your average is: %.2f" % a)

# Calling the main method to run app
main ()
                            
