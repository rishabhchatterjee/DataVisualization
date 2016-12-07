from solveEquations import Equation, solutions
from tkinter import simpledialog

def functionsNormal(mode = 'n'):
    degree = simpledialog.askstring(" ", 'Input degree of polynomial (upto and including 10)')
    for digit in degree:
        if digit not in '0123456789':
            degree = simpledialog.askstring(" ", 'Please input valid degree of polynomial (upto and including 10)')
    while (int(degree) > 10):
        degree = simpledialog.askstring(" ", 'Please input degree 1 <= 10')
    digits = simpledialog.askstring(" ", 'Input maximum value of \'x\'')
    for digit in digits:
        if digit not in '0123456789':
            digits = simpledialog.askstring(" ", 'Please input valid maximum value of \'x\'')
    if(int(digits) == 0):
        digits = simpledialog.askstring(" ", 'Please input non zero maximum value of \'x\'')
    
    A = Equation(degree, mode, digits)
    drawingList = A.makeFunction()
    print('\nEquation entered is y = ', A, '\n', solutions)
    print(drawingList)
    return drawingList

    


