import math, string
from calculateFractions import callWithLargeStack
from tkinter import simpledialog

solutions = set()

class Equation(object):
    def __init__(self, degree, mode = 'n', digits = 100):
        self.degree = int(degree)
        self.mode = mode
        self.digits = digits
        coeffs = ['a','b','c','d','e','f','g','h','i','j']
        self.constant = int(simpledialog.askstring(" ",'Input constant term' ))
        if(self.degree == 1):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 2):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 3):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 4):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 5):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 6):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^6'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.f = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 7):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^7'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^6'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.f = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.g = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 8):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^8'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^7'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^6'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.f = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.g = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.h = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 9):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^9'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^8'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^7'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^6'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.f = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.g = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.h = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.i = int(simpledialog.askstring(" ", 'Input coefficient of x'))
        elif(self.degree == 10):
            self.a = int(simpledialog.askstring(" ", 'Input coefficient of x^10'))
            self.b = int(simpledialog.askstring(" ", 'Input coefficient of x^9'))
            self.c = int(simpledialog.askstring(" ", 'Input coefficient of x^8'))
            self.d = int(simpledialog.askstring(" ", 'Input coefficient of x^7'))
            self.e = int(simpledialog.askstring(" ", 'Input coefficient of x^6'))
            self.f = int(simpledialog.askstring(" ", 'Input coefficient of x^5'))
            self.g = int(simpledialog.askstring(" ", 'Input coefficient of x^4'))
            self.h = int(simpledialog.askstring(" ", 'Input coefficient of x^3'))
            self.i = int(simpledialog.askstring(" ", 'Input coefficient of x^2'))
            self.j = int(simpledialog.askstring(" ", 'Input coefficient of x'))

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
        elif(self.degree == 6):
            return '%dx^6 + %dx^5 + %dx^4 + %dx^3 + %dx^2 +%dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.f, self.constant)
        elif(self.degree == 7):
            return '%dx^7 + %dx^6 + %dx^5 + %dx^4 + %dx^3 + %dx^2 +%dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.constant)
        elif(self.degree == 8):
            return '%dx^8 + %dx^7 + %dx^6 + %dx^5 + %dx^4 + %dx^3 + %dx^2 +%dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.constant)
        elif(self.degree == 9):
            return '%dx^9 + %dx^8 + %dx^7 + %dx^6 + %dx^5 + %dx^4 + %dx^3 + %dx^2 +%dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.constant)
        elif(self.degree == 10):
            return '%dx^10 + %dx^9 + %dx^8 + %dx^7 + %dx^6 + %dx^5 + %dx^4 + %dx^3 + %dx^2 +%dx + %d' %(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.constant)

    def findValuesFunctions(self, f, digits = 10, mode = 'n', count = 0, ans = []):
        global solutions
        if(count >= int(digits)):           
            return []
        else:
            val = f(count)
            if(mode == 'n'):                    # in normal mode append the 
                if(val >= 10):                  # value digit by digit
                    temp = []
                    n = val
                    while(n):
                        temp.append(n % 10)
                        n //= 10
                    temp.reverse()
                    for digit in temp:
                        ans.append(digit)
                else:
                    if(val == 0):               # keeps track of int
                        solutions.add(count)
                    ans.append(val)
            else:                               # appends val (mod 10)
                ans.append(val%10)

            return ans + self.findValuesFunctions(f, digits, self.mode, count + 1, ans = []) 
                                                # recursive call

    def makeFunction(self):                     # returns list with values
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
        elif(self.degree == 6):
            def f(x):
                return self.a*x**6 + self.b*x**5 + self.c*x**4 + self.d*x**3 + self.e*x**2 + self.f*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 7):
            def f(x):
                return self.a*x**7 + self.b*x**6 + self.c*x**5 + self.d*x**4 + self.e*x**3 + self.f*x**2 + self.g*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 8):
            def f(x):
                return self.a*x**8 + self.b*x**7 + self.c*x**6 + self.d*x**5 + self.e*x**4 + self.f*x**3 + self.g*x**2 + self.h*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 9):
            def f(x):
                return self.a*x**9 + self.b*x**8 + self.c*x**7 + self.d*x**6 + self.e*x**5 + self.f*x**4 + self.g*x**3 + self.h*x**2 + self.i*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
        elif(self.degree == 10):
            def f(x):
                return self.a*x**10 + self.b*x**9 + self.c*x**8 + self.d*x**7 + self.e*x**6 + self.f*x**5 + self.g*x**4 + self.h*3 + self.i*x**2 + self.j*x + self.constant
            return callWithLargeStack(self.findValuesFunctions,f, self.digits,self.mode, 0, [])
