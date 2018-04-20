'''The speeding ticket fine policy in Podunksville is $50 plus $5 for
each mph over the limit plus a penalty of $200 for any speed over 90
mph. Write a program that accepts a speed limit and a clocked speed
and either prints a message indicating the speed was legal or prints
the amount of the fine, if the speed is illegal.'''

#04
################################################
##     Zelle 7.6 – computes speeding fine     ##
################################################
sp = 91
limit = 50

# This def with 2 parameters is used to calculate total fee
def fee(speed,speedLimit):
    fee = 50
    diff = (speed - speedLimit) * 5
    fee += diff
    if speed > 90:
        fee += 200
        return fee
    else:
        return fee
    
#  This def is to find out if they even broke the limit or not
def illegal(speed,speedLimit):
    if speed > speedLimit:
        return True
    else:
        return False

# main def
def main():
    if illegal(sp,limit) == True:
        print('You are OVER the speed limit!')
        print('You have been fined for this unacceptable action!')
        print('You now owe, ${}'.format(fee(sp,limit)))
    else:
        print('You were at or under the speed limit at,',sp)

main()
