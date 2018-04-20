# YouTubeVideo Addy https://www.youtube.com/watch?v=GAaSUhPunzM&feature=youtu.be
# Creating my main function
def main ():

    # Putting text out to inform user of what we will do
    print('Find out your average temprature!')

    # Empty line
    print()

    # Taking in 3 inputs from the user and assigning them to variables
    fahr1 = eval(input('Enter your first Fahrenheit: '))
    fahr2 = eval(input('Enter your second Fahrenheit: '))
    fahr3 = eval(input('Enter your third Fahrenheit: '))

    # The equation to average the 3 inputs and assigning it to a variable
    average = (fahr1 + fahr2 + fahr3) / 3

    # Printing out the variable average after it has been calculated
    print ('Your average is: %.1f' % average)

    # Sending the average to a def I have created that calculates
    # fahrenheit to celsius and prints it out
    # The %.1f prints out the float with 1 decimal place
    # conv(average) conv is the def I am calling, average is the
    # variable I am passing through
    print ('Your average in celsius: %.1f' % conv(average))
    print ('Here are your inputs in celsius: ')
    print ('%.1f' % conv(fahr1), '%.1f' % conv(fahr2), '%.1f' % conv(fahr3))

    
# The definition I created to calculate Fahr to Cels
# I created a definition because I was going to be using the
# math equation often and instead of writing it over and over
# I write it once and pass my data through it
def conv (fahrnum):

    # The math equation to convert fahr to cels it stores the output
    # to the variable cels
    cels = (fahrnum - 32) * 5 / 9

    # Returns data in the variable cels so that it may be printed
    return cels

main()
