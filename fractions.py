import string, math
from calculateFractions import *
from tkinter import simpledialog


def getInputs():
    A = Fraction()
    ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
    print(ans)
    return ans

class Fraction(object):

    def __init__(self):
        self.num = simpledialog.askstring(" ", 'Enter numerator of fraction')
        for digit in self.num:
            if digit not in '0123456789':
                self.num = input('\nEnter valid integer please!\n')
        self.den = simpledialog.askstring(" ", 'Enter denominator of fraction')
        for digit in self.den:
            if digit not in '0123456789':
                self.den = simpledialog.askstring(" ", 'Enter valid integer please!')
        while(self.den == '0'):
            self.den = int(simpledialog.askstring(" ", 'Please Enter non 0 denominator'))
        
        self.num = int(self.num)
        self.den = int(self.den)
        self.digits = int(simpledialog.askstring(" ", 'Enter number of decimal places'))

    def __repr__(self):
        return '\nEntered Fraction is %d / %d' %(self.num, self.den)

# A = Fraction()
# ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
# print(ans)
#getInputs()