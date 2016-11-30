from solveEquations import Equation
#from drawTurtle import setup
#from tkinter import *

def functionsNormal(mode = 'n'):
    degree = input('Input degree of polynomial (upto and including 5)\n')
    digits = input('Input maximum \'x\' value of function\n')
    A = Equation(degree, mode, digits)
    drawingList = A.makeFunction()
    print('\nEquation entered is y = ', A, '\n')
    #print(drawingList)
    return drawingList

#print(functionsNormal('n'))
#setup()
    


