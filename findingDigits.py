import math
from math import factorial
from decimal import Decimal, getcontext

################################################################################
#                GET LARGER CALL STACK TO CALC UPTO MANY DIGITS                #
################################################################################

def callWithLargeStack(f,*args):
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

################################################################################
#                CALCULATE UPTO N DIGITS AFTER . FOR RATIONAL NUMBERS          #
################################################################################

def division(divident, divisor, digits = 10, count = 0, ans =[]):
    if(count >= digits):
        return []
    else:
        remainder = divident % divisor
        quotient = divident // divisor
        if(quotient >= 10):
            ans.append((quotient // 10))
            ans.append((quotient % 10))
        else:
            ans.append((quotient))
        nextDivident = remainder*10
        #print('count', count,'divident', divident, 'divisor', divisor, 
        #'quotient', quotient, 'rem', remainder, 'next Divident',nextDivident)
        return  ans + division(nextDivident, divisor, digits, count + 1, ans=[])
#print(callWithLargeStack(division,355,113,1000))
################################################################################
#                 GET RID OF TERMINATING 0'S LEAVING ONE 0                     #
################################################################################

def endingZeroesTerminate(L):
    zeroCount = 0
    if(0 in L):
        first = L.index(0)
        remaining  = len(L) - first 
        for i in range(first, first + remaining):
            if(L[i] == 0):
                zeroCount += 1
        if(zeroCount >= remaining - 1):
            L = L[:first + 1]
        return L
    else:
        return L

################################################################################
#                      COUNT NUMBER OF OCC OF EACH DIGIT                       #
################################################################################

def getDigitsCount(L):
    d = dict()
    for digit in L:
        if(digit in d):
            d[digit] += 1
        else:
            d[digit] = 0
    return d

#print(endingZeroesTerminate(callWithLargeStack(division,355,113, 1000, 0, [])))
#print(endingZeroesTerminate(callWithLargeStack(division,100,4, 10, 0, [])))


################################################################################
#                     GET PI USING CHUDNOVSKY'S ALGORITHM                      #
################################################################################

getcontext().prec=1000

def piChudnovskyAlg(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):   #Chudnovsky algorithm
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
#print(getPiChudnovskyAlg(piChudnovskyAlg(100)))

################################################################################
#                GET DIGITS OCCURING IN VALUES OF A FUNCTION                   #
################################################################################

def findValuesFunctions(f, digits = 10, count = 0, ans = []):
    if(count >= digits):
        return []
    else:
        val = f(count)  
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
        return ans + findValuesFunctions(f, digits, count + 1, ans = [])

def f(x):
    return x**3

#print(findValuesFunctions(f, 10, 0, []))

