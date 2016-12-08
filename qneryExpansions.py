import math 
from tkinter import simpledialog

def qneryExpansion(n, base, ans = []):

    def findReverseAns(n, base, ans = []):
        if (base == 0):
            return [0]
        if(n == 0):
            return []
        elif (n == 1):
            return [1]
        else:
            rem = n % base
            if(rem > 9):
                temp = []
                var = rem
                while(var):
                    temp.append(var % 10)
                    var //= 10
                temp.reverse()
                for digit in temp:
                    ans.append(digit)
            else:
                ans.append(rem)
            n -= rem
            n //= base
            return ans + findReverseAns(n, base, ans = [])

    temp = findReverseAns(n, base)
    print(list(reversed(temp)))
    return list(reversed(temp))

def getNumberBase():
    n = simpledialog.askstring(" ", "Input the number")
    for digit in n:
        if digit not in '0123456789':
            n = simpledialog.askstring("Please enter valid integer!")
   
    n = int(n)

    base = simpledialog.askstring(" ", "Input integer base <= 10")
    for digit in base:
        if(digit not in '0123456789'):
            base = simpledialog.askstring(" ", "Please enter valid base!")
    if (base == '0'):
        base = simpledialog.askstring("Please enter non zero integer!")
    base = int(base)

    return qneryExpansion(n, base)



#print(qneryExpansion(10000023,20))
