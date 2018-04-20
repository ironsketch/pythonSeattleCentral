##def TrthPAndQ():
##    """Generates truth table for and."""
##    print("{:^7}   {:^7}  {:^7}".format("P", "Q ", "P and Q"))
##    print("-"*30)
####             P         Q        P and Q
####    print("  {0}    {1}     {2}  ".format(b1,b2,b1 and b2)
##    for P in [True,False]:
##        for Q in [True,False]:
##            print("{:^7}   {:^7}  {:^7}".format(str(P),str(Q),str(P and Q)))
##            ## print("{:^7}   {:^7}  {:^7}".format(P,Q,P and Q))
##TrthPAndQ()

def troof():
    print("{:^7}   {:^7}   {:^7}   {:^7}   {:^7}   {:^7}   ".format("P", "Q","R","S","PQ o RS","PQ a RS"))
    print("-"*50)
    for P in [True,False]:
        for Q in [True,False]:
            for R in [True,False]:
                for S in [True,False]:
                    print('{:^7}   {:^7}   {:^7}   {:^7}   {:^7}   {:^7}   '.format(str(P),str(Q),str(R),str(S),str((P and Q) or (R and S)),str((P or Q) and (R or S))))
troof()
