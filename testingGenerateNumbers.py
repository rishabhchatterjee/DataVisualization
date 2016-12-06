import turtle
import math
import random
from playingWithPyAudio import *
import threading
from testingScreenshot import takeScreenshot
from solveEquations import solutions
import threading


def draw(drawingList, mode = 'NotFunctionNormal'):
################################################################################
#                            MAKE HEADINGS ETC                                 #
################################################################################
    screen = turtle.Screen()
    screen.title('DATA VISUALIZATION')
    screen.setup(800,800)
    screen.bgcolor('black')
    turtle.shape('turtle')
    turtle.penup()
    turtle.pensize(4)
    turtle.color('white')

    kosbie = turtle.Turtle()
    kosbie.color('orange')
    kosbie.hideturtle()
    kosbie.penup()

    numberTurtle = turtle.Turtle()
    numberTurtle.shape('turtle')
    numberTurtle.color('red')
    numberTurtle.penup()
    numberTurtle.setpos(-385,320)

    extraTurtle = turtle.Turtle()
    extraTurtle.shape('turtle')
    extraTurtle.color('white')
    extraTurtle.penup()
    extraTurtle.setpos(215,320)
    extraTurtle.pendown()
    extraTurtle.write('Takes screenshot when over!', font = 'Arial 10 bold')
    extraTurtle.penup()
    extraTurtle.setpos(-225, 295)
    extraTurtle.write('Integer Solutions (for functions) / index value of 0\'s (for rational and irrational numbers)', font = "Arial 10 bold")
    extraTurtle.hideturtle()

    zeroTurtle = turtle.Turtle()
    zeroTurtle.shape('turtle')
    zeroTurtle.color('pink')
    zeroTurtle.penup()
    zeroTurtle.setpos(-220, 280)


################################################################################
#                           MAKE INNER CIRCLES                                 #
################################################################################
    kosbie.speed(13)
    turtle.speed(13)

    turtle.setpos(0,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()

################################################################################
#                             MAKE NUMBER DICT                                 #
################################################################################

    turtle.setpos(0,-230)
    colors = ['red','violet','tan', 'lightblue', 'green','dark blue', 
                                    'gold', 'deep pink', 'sienna','turquoise']

    numbers = dict()
    for i in range(len(colors)):
        numbers[i] = colors[i]

    numberColors = dict()
    numberColors[0] = ['red', 'indian red', 'dark red', 'orange red', 'red2']
    numberColors[1] = ['violet', 'blue violet', 'dark violet', 'violet red', 
                                                                'pale violet red']
    numberColors[2] = ['tan', 'brown', 'khaki', 'dark khaki', 'khaki1']
    numberColors[3] = ['lightblue', 'light sky blue', 'LightSteelBlue', 
                                                'midnight blue', 'lightblue1']
    numberColors[4] = ['green', 'pale green', 'sea green', 'spring green', 
                                                                'yellow green']
    numberColors[5] = ['dark blue', 'alice blue', 'cadet blue', 'dark slate blue', 
                                                                'deep sky blue']
    numberColors[6] = ['gold', 'yellow', 'light yellow', 'green yellow', 
                                            'light goldenrod yellow', 'yellow4']
    numberColors[7] = ['deep pink', 'pink', 'hot pink', 'light pink', 'pink4']
    numberColors[8] = ['sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4']
    numberColors[9] = ['turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 
                                                                    'turquoise4']

################################################################################
#                           MAKE OUTER CIRCLE                                  #
################################################################################

    turtle.setpos(0,-200)
    turtle.pendown()

    for number in numbers: 
        turtle.color(numbers[number])
        turtle.circle(200,36)

################################################################################
#                               MAKE NUMBERS                                   #
################################################################################

    turtle.penup()
    turtle.setpos(0,-235)
    turtle.color('white')
    turtle.hideturtle()
    for number in numbers:
        turtle.pendown()
        turtle.color(str(numbers[number]))
        turtle.write(str(number), font = 'Times 20 bold')
        turtle.penup()
        turtle.circle(225,36)

    turtle.pensize(1)

################################################################################
#                          SET DIGIT POSITIONS                                 #
################################################################################

    digitPositions = dict()
    digitPositions[0] = [0,128, -200, -153]
    digitPositions[1] = [128, 196, -153, -34]
    digitPositions[2] = [173, 196, -34, 100]
    digitPositions[3] = [68, 173, 100, 187]
    digitPositions[4] = [0, 68, 187, 200]
    digitPositions[5] = [-68, 0, 187, 200]
    digitPositions[6] = [-173, -68, 100, 187]
    digitPositions[7] = [-196, -173, -34, 100]
    digitPositions[8] = [-196, -128, -153, -34]
    digitPositions[9] = [-128, 0, -200, -153]

    def getPosition(digit):

        r = 200
        yLowerBound = digitPositions[digit][2]
        yUpperBound = digitPositions[digit][3]
        y = random.randint(min(yLowerBound, yUpperBound), max(yLowerBound,yUpperBound))
        if digit < 5:
            x = (r**2 - y**2)**0.5
        else:
            x = -(r**2 - y**2)**0.5
        return (x,y)

    turtle.penup()
    turtle.setpos(75,0)

################################################################################
#                           DRAW LINES & DOTS                                  #
################################################################################
    def getDrawingDotPosition(x,y):
        xFactor = random.uniform(1.2,1.3)
        yFactor = random.uniform(1.2,1.3)
        return (x*xFactor, y*yFactor)

    kosbie.speed(12)
    turtle.speed(12)
    turtle.pensize(1)
    numberTurtle.speed(12)
    extraTurtle.speed(12)

    colCount = 0
    shifted = False
    zeroSwapped = False
    zeroRowCount = 1

    def writeSolutions(i,practiceList, color = 'red'):
        index = random.randint(0,4)
        play('zeroSounds/' + str(index) + '.wav')
        (xZero, yZero) = zeroTurtle.position()
        nonlocal zeroRowCount
        if(xZero >= 180):
            yZero -= 12
            xZero = -245
            zeroRowCount += 1
        nonlocal zeroSwapped
        if not zeroSwapped:
            if(yZero <= 260):
                yZero = -276
                xZero = -245
                zeroSwapped = True
        if(zeroRowCount < 8):
            zeroTurtle.color(color)
            zeroTurtle.write(str(i), font = 'Arial 15 bold')
            xZero += 25
            zeroTurtle.penup()
            zeroTurtle.setpos(xZero,yZero)
            zeroTurtle.pendown()
        if(zeroRowCount >= 8):
            zeroTurtle.hideturtle()

    def writeNumbers(i,practiceList, color):
        nonlocal colCount
        nonlocal shifted

        (xNT, yNT) = numberTurtle.position()
        if not shifted:
            if(colCount > 10):
                xNT = 275
                yNT = 320
                shifted = True

        if(yNT <= -308):
            colCount += 1
            xNT += 12
            yNT = 308
        else:
            yNT -= 12

        numberTurtle.penup()
        numberTurtle.setpos(xNT, yNT)
        numberTurtle.pendown()
        numberTurtle.color(color)
        numberTurtle.write(str(practiceList[i]), font = 'Arial 15 bold')

    def drawLines(practiceList, startPosition, i = 0):
        turtle.showturtle()
        if(i == len(practiceList) - 1):
            return
        else:

            endPosition = getPosition(practiceList[i])

            xStartCenterMid = startPosition[0]/2
            yStartCenterMid = startPosition[1]/2
            xEndCenterMid = endPosition[0]/2
            yEndCenterMid = endPosition[1]/2

            color = random.choice(numberColors[practiceList[i]])
            turtle.color(color)

            turtle.penup()
            turtle.setpos(startPosition[0], startPosition[1])
            pos = getDrawingDotPosition(startPosition[0], startPosition[1])
            kosbie.setpos(pos[0], pos[1])       #
            kosbie.color(color)                 #  DRAWS THE DOTS
            kosbie.begin_fill()                 #
            kosbie.circle(random.randint(2,5))  #
            kosbie.end_fill()                   #
            turtle.pendown()

            writeNumbers(i,practiceList, color)
            
            if(mode == 'functionNormal'):
                if(i in solutions):
                    writeSolutions(i,practiceList, color)
            else:
                if(practiceList[i] == 0):
                    writeSolutions(i,practiceList,color)
            
            distance = ((xStartCenterMid - xEndCenterMid)**2 + (yStartCenterMid - yEndCenterMid)**2)**0.5
            
            turtle.pensize(1)
            turtle.goto(xStartCenterMid, yStartCenterMid)
            turtle.pensize(2)
            turtle.goto(xEndCenterMid, yEndCenterMid)
            turtle.pensize(1)
            turtle.goto(endPosition[0], endPosition[1])

            startPosition = endPosition

            drawLines(practiceList,endPosition, i+1)
    
    startPosition = getPosition(drawingList[0])
    drawLines(drawingList, startPosition, 0)
    turtle.hideturtle()
    numberTurtle.hideturtle()
    extraTurtle.hideturtle()
    kosbie.hideturtle()
    turtle.onclick(takeScreenshot())
    turtle.exitonclick()
    turtle.done()

def drawNumbers(drawingList):
    print(drawingList)
    numberTurtle = turtle.Turtle()
    numberTurtle.color('white')
    #numberTurtle.hideturtle()
    numberTurtle.penup()
    numberTurtle.setpos(-300,300)
    for element in drawingList:
        numberTurtle.pendown()
        numberTurtle.write(str(element), font = 'Arial 12 bold')
        numberTurtle.penup()
        (x,y) = numberTurtle.position()
        numberTurtle.setpos(x+5,y)


# draw([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
#  6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 
#  9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 
#  0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 
#  0, 6, 7, 9, 8, 2, 1, 4, 8, 0, 8, 6, 5, 1, 3, 2, 8, 2, 3, 0, 6, 6, 4, 7, 0, 9, 
#  3, 8, 4, 4, 6, 0, 9, 5, 5, 0, 5, 8, 2, 2, 3, 1, 7, 2, 5, 8, 9, 2, 4, 8, 3, 5, 
#  3, 6, 7, 6, 7, 4, 7, 1, 9, 2, 8, 9, 3, 7, 5, 4, 7, 9, 7, 6, 9, 4, 5, 1, 7, 9, 
#  1, 5, 7, 1, 2, 7, 1, 7, 4, 3, 8, 2, 9, 5, 2, 8, 8, 5, 2, 2, 6, 4, 0, 4, 0, 1, 
#  2, 7, 6, 8, 9, 6, 9, 9, 8, 2, 8, 7, 4, 1, 3, 1, 0, 9, 4, 0, 3, 7, 2, 9, 5, 1, 
#  2, 5, 0, 8, 4, 0, 7, 3, 1, 3, 1, 2, 5, 0, 9, 4, 0, 5, 5, 5, 0, 7, 9, 7, 4, 5, 
#  9, 6, 9, 7, 7, 3, 8, 0, 0, 0, 6, 2, 4, 3, 7, 9, 1, 4, 3, 4, 0, 1, 7, 6, 1, 9, 
#  9, 3, 0, 5, 5, 6, 3, 9, 8, 1, 9, 0, 5, 1, 1, 0, 7, 1, 9, 1, 7, 2, 4, 1, 2, 5, 
#  6, 6, 4, 6, 5, 6, 5, 5, 9, 5, 2, 2, 5, 8, 2, 9, 4, 3, 0, 4, 2, 7, 3, 8, 7, 5, 
#  3, 9, 0, 5, 7, 6, 8, 5, 7, 8, 8, 7, 9, 3, 4, 7, 3, 8, 7, 2, 2, 1, 9, 5, 1, 9, 
#  1, 3, 1, 4, 6, 9, 7, 0, 3, 1, 9, 1, 9, 3, 8, 9, 3, 5, 2, 0, 0, 8, 2, 7, 8, 4,
#   8])
#draw([0]*100)
#draw(list(range(10)))
