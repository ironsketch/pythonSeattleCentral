# The main function of the program
def main():

    # Running a for loop 5 times
    for i in range(5):

        # Getting user input each time
        celsius = eval(input("Type in the temp in Celsius: "))

        # Cels to Fahr converter
        fahrenheit = 9.0 / 5.0 * celsius + 32

        # If else conditional to determine unnacceptable answers
        if (fahrenheit > 100):
            print("Gerd Dam dats hot!")
        elif (fahrenheit < 10):
            print("Damn dat cold!")
        else:
            print("meh")
        print("The temp is", fahrenheit, "degrees")
        print()
        
# Calling the main method to run app
main()
