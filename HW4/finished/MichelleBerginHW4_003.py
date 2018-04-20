'''Write and test a function to meet this specification.
squareEach(nums) nums is a list of numbers. Modifies the
list by squaring each entry.'''

#03
################################################
##          Zelle 6.11 - squareEach           ##
################################################

L = [1,4,55,6,84,34,2,354,4365,3,54776]

# Definition to process list (1 parameter)
def squareEach(nums):

    # Initializing a counter to use as location in List
    counter = 0

    # Iteration through items in list nums
    for number in nums:

        # updating number to be the square of it's self
        number = number**2

        # Using counter to insert the updated value back into
        # the same location in List
        nums[counter] = number

        # Plusing counter
        counter += 1

    # Printing new result
    print (nums)

def main():

    # Printing before
    print(L)

    # Sending one parameter to process
    squareEach(L)

main()
