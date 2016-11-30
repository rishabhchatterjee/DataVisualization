import math, string
from calculateFractions import callWithLargeStack
#from playingWithTurtle import *


class Equation(object):
    def __init__(self, degree, mode = 'n', digits = 100):
        self.degree = int(degree)
        self.mode = mode
        self.digits = digits
        coeffs = ['a','b','c','d','e','f','g','h','j','i']
        self.constant = int(input('Input constant term\n'))
        if(self.degree == 1):
            self.a = int(input('Input coefficient of x\n'))
        elif(self.degree == 2):
            self.a = int(input('Input coefficient of x^2\n'))
            self.b = int(input('Input coefficient of x\n'))
        elif(self.degree == 3):
            self.a = int(input('Input coefficient of x^3\n'))
            self.b = int(input('Input coefficient of x^2\n'))
            self.c = int(input('Input coefficient of x\n'))
        elif(self.degree == 4):
            self.a = int(input('Input coefficient of x^4\n'))
            self.b = int(input('Input coefficient of x^3\n'))
            self.c = int(input('Input coefficient of x^2\n'))
            self.d = int(input('Input coefficient of x\n'))
        elif(self.degree == 5):
            self.a = int(input('Input coefficient of x^5\n'))
            self.b = int(input('Input coefficient of x^4\n'))
            self.c = int(input('Input coefficient of x^3\n'))
            self.d = int(input('Input coefficient of x^2\n'))
            self.e = int(input('Input coefficient of x\n'))

    def __repr__(self):
        if(self.degree == 1):
            return '%dx + %d' %(self.a, self.constant)
        elif(self.degree == 2):
            return '%dx^2 + %dx + %d' %(self.a,self.b, self.constant)
        elif(self.degree == 3):
            return '%dx^3 + %dx^2 + %dx + %d' %(self.a, self.b, self.c, self.constant)
        elif(self.degree == 4):
            return  '%dx^4 + %dx^3 + %dx^2 + %dx + %d' %(self.a, self.b, self.c, self.d, self.constant)
        elif(self.degree == 5):
            return '%dx^5 + %dx^4 + %dx^3 + %dx^2 + %dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.constant)

    def findValuesFunctions(self, f, digits = 10, mode = 'n', count = 0, ans = []):
        if(count >= int(digits)):
            return []
        else:
            val = f(count)
            if(mode == 'n'):  
                if(val >= 10):
                    temp = []
                    n = val
                    while(n):
                        temp.append(n % 10)
                        n //= 10
                    temp.reverse()
                    for digit in temp:
                        ans.append(digit)
                else:
                    ans.append(val)
            else:
                ans.append(val%10)

            return ans + self.findValuesFunctions(f, digits, self.mode, count + 1, ans = [])

    def makeFunction(self):
        if(self.degree == 1):
            def f(x):
                return self.a*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 2):
            def f(x):
                return self.a*x**2 + self.b*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 3):
            def f(x):
                return self.a*x**3 + self.b*x**2 + self.c*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 4):
            def f(x):
                return self.a*x**4 + self.b*x**3 + self.c*x**2 + self.d*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 5):
            def f(x):
                return self.a*x**5 + self.b*x**4 + self.c*x**3 + self.d*x**2 + self.e*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])

# degree = input('Input degree of polynomial (upto and including 5)\n')
# A = Equation(degree, 'm', 1)
# print(A, '\n\n',A.makeFunction())




