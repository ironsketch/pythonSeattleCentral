# Write a function aGreetsb (a,b), which has a introduce
# themselves to b and b introduce themselves to a.

# The definition here is taking in a variable and using that variable as person.
# When the variable comes in, in () it is used as the definitions () in
# this case, person. It then uses that variable in the definition it's self.
def greeting(person):
    print ("Heyo"), person
    print ("How are you?")

# Below is the definition being used 2 times with the information Melanie and
# Jake passed through. It then follows what the definition says to do, in this
# case it says to print out Heyo and the persons name etc.
greeting("Melanie")
greeting("Jake")

# Finally this time we take in the users name and send that as a variable that
# stores the information they typed, to the definition to process!
newuser = raw_input("Enter your name: ")
greeting(newuser)
