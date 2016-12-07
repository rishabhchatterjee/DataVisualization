import turtle
import math
import random
from playingWithPyAudio import *
from testingScreenshot import takeScreenshot
from solveEquations import solutions


def draw(drawingList, mode = 'NotFunctionNormal'):
################################################################################
#                            MAKE HEADINGS ETC                                 #
################################################################################
    screen = turtle.Screen()
    screen.title('DATA VISUALIZATION')
    screen.setup(800,800)
    screen.bgcolor('black')
    turtle.shape('turtle')              # turtle for gradient and network
    turtle.penup()
    turtle.pensize(4)
    turtle.color('white')

    kosbie = turtle.Turtle()            # turtle for scatterplot
    kosbie.color('orange')
    kosbie.hideturtle()
    kosbie.penup()

    numberTurtle = turtle.Turtle()      # turtle to write numbers
    numberTurtle.shape('turtle')
    numberTurtle.color('red')
    numberTurtle.penup()
    numberTurtle.setpos(-385,320)

    extraTurtle = turtle.Turtle()       # turtle to write solutions
    extraTurtle.shape('turtle')
    extraTurtle.color('white')
    extraTurtle.penup()
    extraTurtle.setpos(-70,320)
    extraTurtle.pendown()
    extraTurtle.write('Takes screenshot when over!', font = 'Arial 10 bold')
    extraTurtle.penup()
    extraTurtle.setpos(-225, 295)
    extraTurtle.write('Integer Solutions (for functions) / index value of 0\'s (for rational and irrational numbers)', 
                font = "Arial 10 bold")
    extraTurtle.hideturtle()

    zeroTurtle = turtle.Turtle()
    zeroTurtle.shape('turtle')
    zeroTurtle.color('pink')
    zeroTurtle.penup()
    zeroTurtle.setpos(-220, 280)


################################################################################
#                           MAKE INNER CIRCLES                                 #
################################################################################
    kosbie.speed(13)                    # set speed while drawing setup
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

    for i in range(len(colors)):    # set a color family for each digit
        numbers[i] = colors[i]

    numberColors = dict()           # give shades of color family to each digit

    numberColors[0] = ['red', 'indian red', 'dark red', 'orange red', 'red2']
    numberColors[1] = ['violet', 'blue violet', 'dark violet', 'violet red', 
                                                             'pale violet red']
    numberColors[2] = ['tan', 'brown', 'khaki', 'dark khaki', 'khaki1']
    numberColors[3] = ['lightblue', 'light sky blue', 'LightSteelBlue', 
                                                'midnight blue', 'lightblue1']
    numberColors[4] = ['green', 'pale green', 'sea green', 'spring green', 
                                                                'yellow green']
    numberColors[5] = ['dark blue', 'alice blue', 'cadet blue', 
                                            'dark slate blue', 'deep sky blue']
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
        turtle.circle(200,36)           # 10 digits covering 360 degrees

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

    digitPositions = dict()                     # x,y coord of starting and 
    digitPositions[0] = [0,128, -200, -153]     # ending points of each digit's
    digitPositions[1] = [128, 196, -153, -34]   # arc on the circle
    digitPositions[2] = [173, 196, -34, 100]
    digitPositions[3] = [68, 173, 100, 187]
    digitPositions[4] = [0, 68, 187, 200]
    digitPositions[5] = [-68, 0, 187, 200]
    digitPositions[6] = [-173, -68, 100, 187]
    digitPositions[7] = [-196, -173, -34, 100]
    digitPositions[8] = [-196, -128, -153, -34]
    digitPositions[9] = [-128, 0, -200, -153]

    def getPosition(digit):                 # alg to get random point on arc
        r = 200                             # of needed digit
        yLowerBound = digitPositions[digit][2]
        yUpperBound = digitPositions[digit][3]
        y = random.randint(min(yLowerBound, yUpperBound), 
                                    max(yLowerBound,yUpperBound))
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

    def getDrawingDotPosition(x,y):         # get random point behind the digit
        xFactor = random.uniform(1.2,1.3)   # in a particular space to draw dot
        yFactor = random.uniform(1.2,1.3)
        return (x*xFactor, y*yFactor)

    kosbie.speed(12)                # reset all turtle's speed so that they 
    turtle.speed(12)                # work at same pace simultaneously
    turtle.pensize(1)
    numberTurtle.speed(12)
    extraTurtle.speed(12)

    colCount = 0
    shifted = False
    zeroSwapped = False
    zeroRowCount = 1
    (xTemp, yTemp) = zeroTurtle.position()
    zeroTurtle.setpos(-230, yTemp)

    def writeSolutions(i,practiceList, color = 'red'):
        index = random.randint(0,4)         # 5 different sounds
        play('zeroSounds/' + str(index) + '.wav')
        (xZero, yZero) = zeroTurtle.position()
        nonlocal zeroRowCount
        if(xZero >= 180):                   # when reaches end of one row
            yZero -= 12
            xZero = -265
            zeroRowCount += 1
        nonlocal zeroSwapped
        if not zeroSwapped:                 # shift to bottom so that main 
            if(yZero <= 260):               # picture doesn't coincide
                yZero = -276
                xZero = -265
                zeroSwapped = True
        if(zeroRowCount < 8):               # set limit to number of rows
            zeroTurtle.color(color)         # of solutions
            zeroTurtle.write(str(i), font = 'Arial 15 bold')
            xZero += 35
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
            if(colCount > 10):          # shift to right to avoid overlap with
                xNT = 275               # main pic
                yNT = 320
                shifted = True
        if(yNT <= -308):                # end of one col
            colCount += 1
            xNT += 10
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
            xStartCenterMid = startPosition[0]/2        # intermediate coords
            yStartCenterMid = startPosition[1]/2
            xEndCenterMid = endPosition[0]/2
            yEndCenterMid = endPosition[1]/2
            color = random.choice(numberColors[practiceList[i]])
            turtle.color(color)
            turtle.penup()
            turtle.setpos(startPosition[0], startPosition[1])
            pos = getDrawingDotPosition(startPosition[0], startPosition[1])
            kosbie.setpos(pos[0], pos[1])       #
            kosbie.color(color)                 #  draws scatterplot
            kosbie.begin_fill()                 #
            kosbie.circle(random.randint(2,5))  #
            kosbie.end_fill()                   #
            turtle.pendown()
            writeNumbers(i,practiceList, color)
            if(mode == 'functionNormal'):       # writes int sols in range
                if(i in solutions):
                    writeSolutions(i,practiceList, color)
            else:
                if(practiceList[i] == 0):
                    writeSolutions(i,practiceList,color)
            distance = ((xStartCenterMid - xEndCenterMid)**2 + 
                                (yStartCenterMid - yEndCenterMid)**2)**0.5
            turtle.pensize(1)
            turtle.goto(xStartCenterMid, yStartCenterMid) # starts gradient
            turtle.pensize(2)
            turtle.goto(xEndCenterMid, yEndCenterMid)     # draws network
            turtle.pensize(1)
            turtle.goto(endPosition[0], endPosition[1])   # ends gradient
            startPosition = endPosition
            drawLines(practiceList,endPosition, i+1)      # recursive call
    
    startPosition = getPosition(drawingList[0]) 
    drawLines(drawingList, startPosition, 0)        # function call is here
    turtle.hideturtle()                     #
    numberTurtle.hideturtle()               #   hides turtles after drawing
    extraTurtle.hideturtle()                #   is over
    kosbie.hideturtle()                     #
    turtle.onclick(takeScreenshot())             # takes automatic screenshot
    turtle.exitonclick()
    turtle.done()

#draw(list(range(20)))