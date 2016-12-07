from functionsNormal import functionsNormal
from fractions import *
from piDigits import *
from testFreeDrawing import *
from qneryExpansions import *
from testingGenerateNumbers import *
from tkinter import *
from tkinter import simpledialog
import turtle
from testingScreenshot import takeScreenshot

## Template adapted from barebones.py on course website ##

def init(data):
    data.mode = 'splashScreen'
    data.background = PhotoImage(file = 'images/mathstats.gif')
    data.functionsBackground = PhotoImage(file = 'images/Functions.gif')
    data.fractionsBackground = PhotoImage(file = 'images/f.gif')
    data.piBackground = PhotoImage(file = 'images/PI.gif')
    data.qnaryBackground = PhotoImage(file = 'images/binary.gif')
    data.functionsPageLoaded = False

def mousePressed(event, data):
    (x,y) = (event.x, event.y)

    if(data.width - 100 <= x <= data.width - 50 and 50 <= y <= 100):
        init(data)

    if( 30 <= x <= 110 and 20 <= y <= 70):
        data.mode = 'help'

    if( 150 <= x <= 230 and 20 <= y <= 70):
        data.mode = 'aboutUs'

    if(data.mode == 'splashScreen'):
        if(data.width//2 - 300 <= x <= data.width//2 - 25 and data.height//2 - 80 <= y <= data.height//2 - 20):
            data.mode = 'functions'
        if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 - 80 <= y <= data.height//2 - 20):
            data.mode = 'fractions'
        if(data.width//2 - 300 <= x <= data.width//2 -25 and data.height//2 + 30 <= y <= data.height//2 + 90):
            data.mode = 'pi'
        if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 + 30 <= y <= data.height//2 + 90):
            data.mode = 'freeDraw'
        if(data.width//2 - 162.5 <= x <= data.width//2 + 112.5 and data.height//2 + 130 <= y <= data.height//2 + 190):
            data.mode = 'qnaryNumbers'

    if(data.mode == 'functions'):
        if(data.functionsPageLoaded == True):
            if(data.width//2 - 300 <= x <= data.width//2 - 25 and data.height//2 - 10 <= y <= data.height//2 + 50):
                drawingList = functionsNormal('n')
                draw(drawingList, 'functionNormal')
            if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 - 10 <= y <= data.height//2 + 50):
                drawingList = functionsNormal('m')
                draw(drawingList,'notFunctionNormal') 

    if(data.mode == 'fractions'):
        if(data.width//2 - 100 <= x <= data.width//2 + 100 and data.height//2 - 100 <= y <= data.height//2 + 100):
            drawingList = getInputs()
            draw(drawingList)

    if(data.mode == 'pi'):
        if(data.width//3 - 200 <= x <= data.width//3 + 75 and data.height//3 <= y <= data.height//3 + 60):
            drawingList = piDigitsList('c')
            draw(drawingList)

        if(data.width//3 + 200 <= x <= data.width//3 + 475 and data.height//3 <= y <= data.height//3 + 60):
            drawingList = piDigitsList('r')
            draw(drawingList)

    if(data.mode == 'freeDraw'):
        if(data.width//2 - 137.5 <= x <= data.width//2 + 137.5 and data.height//2 - 30 <= y <= data.height//2 + 30):
            freeDraw()

    if(data.mode == 'qnaryNumbers'):
        if( 100 <= x <= 700 and 250 <= y <= 550):
            drawingList = getNumberBase()
            draw(drawingList)
        
# keyPressed is for debugging purposes but works too

def keyPressed(event, data):
    if(event.keysym == 'h'):
        data.mode = 'splashScreen'
        data.functionsPageLoaded = False

    if(data.mode == 'splashScreen'):
        if(event.keysym == 'f'):
            data.mode = 'functions'
        elif(event.keysym == 'q'):
            data.mode = 'fractions'
        elif(event.keysym == 'p'):
            data.mode = 'pi'
        elif(event.keysym == 'd'):
            data.mode = 'freeDraw'

    if(data.mode == 'functions'):
        if(event.keysym == 'n'):
            drawingList = functionsNormal('n')
            draw(drawingList)

        if(event.keysym == 'm'):
            drawingList = functionsNormal('m')
            draw(drawingList)
            
    if(data.mode == 'fractions'):
        if(event.keysym == 'space'):
            drawingList = getInputs()
            draw(drawingList)

    if(data.mode == 'pi'):
        if(event.keysym == 'c'):
            drawingList = piDigitsList('c')
            draw(drawingList)
        if(event.keysym == 'r'):
            drawingList = piDigitsList('r')
            draw(drawingList)

    if data.mode == 'freeDraw':
        freeDraw()


def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(400,400, image = data.background)
    canvas.create_rectangle(data.width - 100, 50, data.width - 50, 100, fill = 'yellow', width = 0)
    canvas.create_polygon(data.width - 110, 50, data.width - 40, 50, data.width - 75, 15, fill = 'dark green', width = 0)
    canvas.create_rectangle(data.width - 90, 60, data.width - 80, 70)
    canvas.create_rectangle(data.width - 70, 60, data.width - 60, 70)
    canvas.create_text(data.width - 75, 90, text = 'HOME', font = 'Arial 10 bold', fill = 'red')

    def help():
        canvas.create_rectangle(30, 20, 110,70, width = 1, outline = 'red')
        canvas.create_text(70, 45, text = 'HELP', font = "Arial 13 bold")

    def aboutUs():
        canvas.create_rectangle(150, 20, 230,70, width = 1, outline = 'red')
        canvas.create_text(190, 45, text = 'ABOUT US', font = "Arial 13 bold")

    if(data.mode == 'splashScreen'):
        canvas.create_text(data.width//2, data.height//4 + 25, 
                                text = "Welcome to Data Visualization",
                                    font = "Arial 26 bold")

        canvas.create_rectangle(data.width//2 - 300, data.height//2 - 80, data.width//2 - 25, data.height//2 - 20)
        canvas.create_text(data.width//2 - 170, data.height//2 - 50, text = "Functions", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 + 25, data.height//2 - 80, data.width//2 + 300, data.height//2 - 20)
        canvas.create_text(data.width//2 + 170, data.height//2 - 50, text = "Fractions", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 - 300, data.height//2 + 30, data.width//2 -25, data.height//2 + 90)
        canvas.create_text(data.width//2 - 170, data.height//2 + 60, text = "PI <3", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 + 25, data.height//2 + 30, data.width//2 + 300, data.height//2 + 90)
        canvas.create_text(data.width//2 + 170, data.height//2 + 60, text = "Scratchpad", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 - 162.5, data.height//2 + 130, data.width//2 + 112.5, data.height//2 + 190)
        canvas.create_text(data.width//2 - 20, data.height//2 + 160, text = "Qnary Expansions", font = "Arial 20 bold", fill = 'red')

        help()
        aboutUs()

    if(data.mode == 'functions'):
        canvas.create_image(400,275, image = data.functionsBackground)
        canvas.create_text(data.width//2, data.height//4, 
                                text = "Let us visualize functions!",
                                    font = "Arial 26 bold")

        canvas.create_rectangle(data.width//2 - 300, data.height//2 - 10, data.width//2 - 25, data.height//2 + 50)
        canvas.create_text(data.width//2 - 170, data.height//2 + 20, text = "Normal Mode", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 + 25, data.height//2 - 10, data.width//2 + 300, data.height//2 + 50)
        canvas.create_text(data.width//2 + 170, data.height//2 + 20, text = "Modular Arithmetic Mode", font = "Arial 20 bold", fill = 'red')

        canvas.create_text(data.width//2, data.height - 250, 
            text = 'Normal Mode : In this mode the values of the function \nis evaluated and each digit (if value >= 10) is visualized\n',
                font = 'Arial 20 bold', fill = 'blue')
        
        canvas.create_text(data.width//2, data.height - 200, 
            text = 'Modular Arithemtic Mode : In this mode the values of the function \nis evaluated and the one\'s digit (found by mod 10) is visualized',
                font = 'Arial 20 bold', fill = 'blue')
        help()
        aboutUs()
        data.functionsPageLoaded = True

    if(data.mode == 'fractions'):
        canvas.create_image(400,400, image = data.fractionsBackground)
        canvas.create_text(data.width//2, data.height//4,
                                text = "Let us visualize fractions!",
                                    font = " Arial 24 bold")
        canvas.create_text(data.width//2, data.height//4 + 35,
                                text = "Click the fraction to start!",
                                    font = " Arial 24 bold")
        help()
        aboutUs()

    if(data.mode == 'pi'):
        canvas.create_image(400,500, image = data.piBackground)
        canvas.create_text(data.width//2, data.height//5,
                                text = "Let us visualize Pi!",
                                    font = " Arial 24 bold")

        canvas.create_rectangle(data.width//3 - 200, data.height//3, data.width//3 + 75, data.height//3 + 60)
        canvas.create_text(data.width//3 - 62.5, data.height//3 + 30, text = 'Chudnovsky Algorithm',
                                font= 'Arial 20 bold', fill = 'red')

        canvas.create_rectangle(data.width//3 + 200, data.height//3, data.width//3 + 475, data.height//3 + 60)
        canvas.create_text(data.width//3 + 337.5, data.height//3 + 30, text = 'Recursive Algorithm',
                                font= 'Arial 20 bold', fill = 'red')
        help()
        aboutUs()
    
    if(data.mode == 'freeDraw'):
        canvas.create_rectangle(data.width//2 - 137.5, data.height//2 - 30, data.width//2 + 137.5, data.height//2 + 30)
        canvas.create_text(data.width//2, data.height//2, text = "Scratchpad",
                                    font = 'Arial 20 bold', fill = 'red')
        help()
        aboutUs()

    if(data.mode == 'qnaryNumbers'):
        canvas.create_image(400,400, image = data.qnaryBackground)
        canvas.create_text(data.width//2, 200, text = "Click the hands to start!",font= 'Arial 20 bold', fill = 'red' )
        help()
        aboutUs()

    text = '''\
    Welcome to Data Visualization! This program has 5 modes as shown below.

    First, Functions mode. Functions mode has two sub-modes, Normal and Modular Arithemtic 
    Mode as explained on the Functions page.This mode evaluates a function in the given range 
    of \'x\' values (the maximum \'x\' value input which you enter) and visualizes it as per 
    the sub-mode.

    Second, Fractions mode. Fractions mode let's you input a numerator, denominator, and 
    number of digits you wish to visualize. Using a recursive algorithm, the program 
    evaluates the quotient as many times as the maximum digits you have inputted. The 
    algorithm stops the visualization the moment it notices five or more 0\'s\'s 
    consecutively after the decimal point.

    Third, Pi <3 mode. Pi mode has two sub-modes, Chudnovsky Algorithm (used to calculate)
    the n-th digit after the decimal point using a formula), and a Recursive Algorithm,
    which works on the same principle as recursive division for fractions. You will be 
    prompted to input number of digits after decimal point to calculate till.

    Fourth, Scratchpad. This mode allows you to draw whatever you want! Feel
    free and let your imagination flow!

    Fifth, Qnery Expansions. This mode allows you to input any number and any
    base and converts the number to the form in that base!

    NOTE: The program will automatically take a Screenshot of what you have visualized
    save it to the current folder (directory) you are in! Also, it will make a sound
    whenerver a solution / zero is encountered!
    '''
    if(data.mode == 'help'):
        canvas.create_text(data.width//2, data.height//6, text = "HELP MODE", font = "Arial 20 bold underline", fill ='red')
        canvas.create_text(data.width//3 + 100, data.height//3 + 125,
                        text = text, font = 'Arial 15 bold')
        aboutUs()

    aboutUsText = '''\
    Numbers are beautiful. However, their beauty is hidden in their 'raw' form. When we 
    see them as simple digits, we cannot understand their potential - what they can represent. 

    This program helps us do two things, first visualize the numbers, and second see 
    the beauty of numbers. It uses modular arithmetic (if mode is selected) and recursive
    division and drawing to make a network representing how functions, rational, and 
    irrational numbers behave with time. 

    Using the drawing algorithm, three types of  networks are made - one is a line 
    gradient, second is a circular network, and third is a scatterplot - all on the 
    same page, simultaneously. Along with this, it makes a sound whenever a solution
    or zero is encountered (as depending on the mode) and prints out the solution
    or the index value of the zero.
    '''
    if(data.mode == 'aboutUs'):
        canvas.create_text(data.width//2, data.height//6, text = "ABOUT US", font = "Arial 20 bold underline", fill ='red')
        canvas.create_text(data.width//3 + 100, data.height//3 + 50,
                        text = aboutUsText, font = 'Arial 15 bold')   
        canvas.create_text(data.width//2 + 320, data.height//2 + 250, 
                            text = 'Rishabh Chatterjee \nDec. 2016 (c)', font = 'Arial 9 bold')
        help()     

    
####################################
# use the run function as-is
####################################

def DataVisualization(width=300, height=300):                 
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas

    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    init(data)

    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Thank You!")

DataVisualization(800, 800)