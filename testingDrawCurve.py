import turtle
import math
import random
from playingWithPyAudio import *


def draw(drawingList):

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

################################################################################
#                           MAKE INNER CIRCLES                                 #
################################################################################
    kosbie.speed(13)
    turtle.speed(13)

    # turtle.setpos(0,-25)
    # turtle.pendown()
    # turtle.begin_fill()
    # turtle.circle(25)
    # turtle.end_fill()
    # turtle.penup()
    # turtle.setpos(0,-50)
    # turtle.pendown()
    # turtle.circle(50)
    # turtle.penup()
    # turtle.setpos(0,-75)
    # turtle.pendown()
    # turtle.circle(75)
    # turtle.penup()
    # # turtle.setpos(0,-300)
    # # turtle.pendown()
    # # turtle.circle(300)
    # # turtle.penup()

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
    #turtle.hideturtle()
    for number in numbers:
        turtle.pendown()
        turtle.color(str(numbers[number]))
        turtle.write(str(number), font = 'Times 20 bold')
        turtle.penup()
        turtle.circle(225,36)

    #turtle.hideturtle()
    turtle.pensize(1)

################################################################################
#                          SET DIGIT POSITIONS                                 #
################################################################################

    # (0.00,-200.00)(128.56,-153.21)
    # (128.56,-153.21)(196.96,-34.73)
    # (196.96,-34.73)(173.21,100.00)
    # (173.21,100.00)(68.40,187.94)
    # (68.40,187.94)(-68.40,187.94)
    # (-68.40,187.94)(-173.21,100.00)
    # (-173.21,100.00)(-196.96,-34.73)
    # (-196.96,-34.73)(-128.56,-153.21)
    # (-128.56,-153.21)(-0.00,-200.00)
    # (-0.00,-200.00)

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
        y = random.randint(yLowerBound, yUpperBound)
        if digit < 5:
            x = (r**2 - y**2)**0.5
        else:
            x = -(r**2 - y**2)**0.5
        return (x,y)

    turtle.penup()
    turtle.setpos(0,0)

################################################################################
#                           DRAW LINES & DOTS                                  #
################################################################################
    def getDrawingDotPosition(x,y):
        xFactor = random.uniform(1.3,1.5)
        yFactor = random.uniform(1.3,1.5)
        return (x*xFactor, y*yFactor)

    #startPosition = getPosition(drawingList[0])

    def playSound(d):
        if(d == 0): return w0
        if(d == 1): return w1
        if(d == 2): return w2
        if(d == 3): return w3
        if(d == 4): return w4
        if(d == 5): return w5
        if(d == 6): return w6
        if(d == 7): return w7
        if(d == 8): return w8
        if(d == 9): return w9

    kosbie.speed(13)
    turtle.speed(13)

    def kochSide(length, n):
        if (n == 1):
            turtle.forward(length)
            #turtle.goto(ending)
        else:
            kochSide(length/3.0, n-1)
            turtle.left(60)
            kochSide(length/3.0, n-1)
            turtle.right(120)
            kochSide(length/3.0, n-1)
            turtle.left(60)
            kochSide(length/3.0, n-1)

    def drawLines(practiceList, startPosition, i = 0):
        if(i == len(practiceList) - 1):
            return
        else:
            endPosition = getPosition(practiceList[i+1])

            xStartCenterMid = startPosition[0]/2
            yStartCenterMid = startPosition[1]/2
            xEndCenterMid = endPosition[0]/2
            yEndCenterMid = endPosition[1]/2

            color = random.choice(numberColors[practiceList[i]])
            turtle.color(color)

            #play('saxSounds/' + str(practiceList[i]) + '.wav')
            #play(playSound(practiceList[i]))
            turtle.penup()
            turtle.setpos(startPosition[0], startPosition[1])
            pos = getDrawingDotPosition(startPosition[0], startPosition[1])
            kosbie.setpos(pos[0], pos[1])       #
            kosbie.color(color)                 #  DRAWS THE DOTS
            kosbie.begin_fill()                 #
            kosbie.circle(random.randint(2,5))  #
            kosbie.end_fill()                   #
            #kosbie.write(str(practiceList[i]), font = 'Times 20 bold')
            turtle.pendown()

            turtle.goto(xStartCenterMid, yStartCenterMid)
            turtle.goto(xEndCenterMid, yEndCenterMid)
            turtle.goto(endPosition[0], endPosition[1])

            startPosition = endPosition
            #turtle.right(angleShift)
            drawLines(practiceList,endPosition, i+1)

    drawLines(drawingList, getPosition(drawingList[0]), 0)

#turtle.circle(50, -180)

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
#draw([1,2,3,4,5,6,7,8,9])