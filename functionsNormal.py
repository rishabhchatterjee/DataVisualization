from solveEquations import Equation
#from drawTurtle import setup
from tkinter import simpledialog

def functionsNormal(mode = 'n'):
    degree = simpledialog.askstring(" ", 'Input degree of polynomial (upto and including 10)')
    while (int(degree) > 10):
        degree = simpledialog.askstring(" ", 'Please input degree 1 <= 10')
    digits = simpledialog.askstring(" ", 'Input maximum value of \'x\'')
    A = Equation(degree, mode, digits)
    drawingList = A.makeFunction()
    print('\nEquation entered is y = ', A, '\n')
    print(drawingList)
    return drawingList

#print(functionsNormal('n'))
#setup()
    


