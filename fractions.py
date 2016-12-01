import string, math
from calculateFractions import *


def getInputs():
    A = Fraction()
    ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
    print(ans)
    return ans

class Fraction(object):

    def __init__(self):
        self.num = (input('\nEnter numerator of fraction\n'))
        for digit in self.num:
            if digit not in '0123456789':
                self.num = input('\nEnter valid integer please!\n')
        self.den = (input('\nEnter denominator of fraction\n'))
        for digit in self.den:
            if digit not in '0123456789':
                self.den = input('\nEnter valid integer please!\n')
        while(self.den == '0'):
            self.den = int(input("\nPlease Enter non 0 denominator\n"))
        
        self.num = int(self.num)
        self.den = int(self.den)
        self.digits = int(input('\nEnter number of decimal places\n'))

    def __repr__(self):
        return '\nEntered Fraction is %d / %d' %(self.num, self.den)

# A = Fraction()
# ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
# print(ans)
#getInputs()