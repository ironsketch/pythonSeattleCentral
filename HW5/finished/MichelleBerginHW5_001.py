#01
################################################
##     Zelle 7.1. – compute wages with OT     ##
################################################

# Definition to calculate wage and OT
def wages(OT,wage,hours):
    earned = 0

    # If the hours hit to Overtime pay, then
    if hours > 40:

        # Find how much was overtime
        remainder = hours - 40

        # Calculate how much you made before overtime
        earned = wage * 40

        # Calculate what rate is your overtime based on your hourly
        OT *= wage

        # Then add the rest all together to get total earned
        earned = (OT * remainder) + earned
        return earned
    else:
        # Or you made 40 or less and it returns what you  made
        earned = wage * hours
        return earned

print (wages(1.5,10,41))
