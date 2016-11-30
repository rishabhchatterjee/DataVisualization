import string, math
from calculateFractions import *


def getInputs():
    A = Fraction()
    ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
    print(ans)
    return ans

class Fraction(object):

    def __init__(self):
        self.num = int(input('Enter numerator of fraction\n'))
        self.den = int(input('\nEnter denominator of fraction\n'))
        
        while(self.den == 0):
            self.den = int(input("\nPlease Enter non 0 denominator\n"))

        self.digits = int(input('\nEnter number of decimal places\n'))

    def __repr__(self):
        return '\nEntered Fraction is %d / %d' %(self.num, self.den)

# A = Fraction()
# ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
# print(ans)
#getInputs()