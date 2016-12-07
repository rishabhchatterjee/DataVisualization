import string, math
from calculateFractions import *
from tkinter import simpledialog

class Fraction(object):

    def __init__(self):
        self.num = simpledialog.askstring(" ", 'Enter numerator of fraction')
        for digit in self.num:              # checks valid input
            if digit not in '0123456789':
                self.num = simpledialog.askstring(" ",'Enter valid integer please!')

        self.den = simpledialog.askstring(" ", 'Enter denominator of fraction')
        for digit in self.den:
            if digit not in '0123456789':
                self.den = simpledialog.askstring(" ", 'Enter valid integer please!')
        while(self.den == '0'):             # checks non zero denominator
            self.den = int(simpledialog.askstring(" ", 'Please Enter non 0 denominator'))
        
        self.num = int(self.num)
        self.den = int(self.den)
        self.digits = (simpledialog.askstring(" ", 'Enter number of decimal places'))
        for digit in self.digits:
            if digit not in '0123456789':
                self.digits = simpledialog.askstring(" ", 'Enter valid integer please!')
        self.digits = int(self.digits)
        if(self.digits == 0):
            self.digits = int(simpledialog.askstring(" ", 'Enter non zero integer please!'))

    def __repr__(self):
        return '\nEntered Fraction is %d / %d' %(self.num, self.den)

def getInputs():
    A = Fraction()
    ans = endingZeroesTerminate((callWithLargeStack(division,A.num,A.den,A.digits)))   
    print(ans)
    return ans
