#Formula to calculate compound interest annually is given by:
# A = P(1 + R/100) t
# Compound Interest = A – P
# Where, A is amount ,P is principle amount, R is the rate and T is the time span
def compoundinterst(P,t,R):
    A=P*(pow((1+R/100),t))
    
    compoundint=A-P
    return compoundint
print(compoundinterst(10000,5,10.25))