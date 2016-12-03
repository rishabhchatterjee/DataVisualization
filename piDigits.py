import math, random
from calculateFractions import callWithLargeStack, division
from math import factorial
from decimal import Decimal, getcontext
from tkinter import simpledialog

def piDigitsList(mode = 'r'):
    digits = int(simpledialog.askstring(" ", "Enter number of decimal places"))
    #digits = int(input("Enter number of decimal places\n"))
    if(mode == 'r'):
        ans = callWithLargeStack(division, 355, 113, digits)
        print(ans)

    if(mode == 'c'):

        getcontext().prec=digits

        def piChudnovskyAlg(n): #Chudnovsky algorithm
            t = Decimal(0)
            pi = Decimal(0)
            deno = Decimal(0)
            k = 0
            for k in range(n):   
                t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
                deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
                pi += Decimal(t)/Decimal(deno)                                   
            pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
            pi = 1/pi
            return pi

        def getPiChudnovskyAlg(n):
            pi = str(n)
            piDigitList = []
            for digit in pi:
                if digit != '.':
                    piDigitList.append(int(digit))
            return piDigitList
        ans = (getPiChudnovskyAlg(piChudnovskyAlg(10)))
        print(ans)
        return ans

#print(piDigitsList('c'))
