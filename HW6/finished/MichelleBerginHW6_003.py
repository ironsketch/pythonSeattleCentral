#03
################################################
##                  Zelle 8.3                 ##
################################################

def double(investment,r):
    a = 0
    t = 0

    # While the investment is less than twice its self
    while a < investment * 2:
        # Calculate the investment
        a = investment * (1 + r * t)

        # Calculating by year and adding one
        t += 1
    print (t,a)
        
inv =10000.00
double(inv,3.875)
