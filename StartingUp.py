# events-example0.py
# Barebones timer, mouse, and keyboard events
from functionsNormal import functionsNormal
from fractions import *
from piDigits import *
from testFreeDrawing import *
#from draw import *
from testingDrawCurve import *
from tkinter import *
from tkinter import simpledialog
import turtle

####################################
# customize these functions
####################################
def init(data):
    data.mode = 'splashScreen'
    data.background = PhotoImage(file = 'images/mathstats.gif')
    data.functionsBackground = PhotoImage(file = 'images/Functions.gif')
    data.fractionsBackground = PhotoImage(file = 'images/f.gif')
    data.piBackground = PhotoImage(file = 'images/PI.gif')
    data.functionsPageLoaded = False

def mousePressed(event, data):
    (x,y) = (event.x, event.y)

    if(data.width - 100 <= x <= data.width - 50 and 50 <= y <= 100):
        init(data)

    if(data.mode == 'splashScreen'):
        if(data.width//2 - 300 <= x <= data.width//2 - 25 and data.height//2 - 10 <= y <= data.height//2 + 50):
            data.mode = 'functions'
        if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 - 10 <= y <= data.height//2 + 50):
            data.mode = 'fractions'
        if(data.width//2 - 300 <= x <= data.width//2 -25 and data.height//2 + 100 <= y <= data.height//2 + 160):
            data.mode = 'pi'
        # canvas.create_rectangle(data.width//2 + 25, data.height//2 + 100, data.width//2 + 300, data.height//2 + 160)
        if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 + 100 <= y <= data.height//2 + 160):
            data.mode = 'freeDraw'

    if(data.mode == 'functions'):
        if(data.functionsPageLoaded == True):
            if(data.width//2 - 300 <= x <= data.width//2 - 25 and data.height//2 - 10 <= y <= data.height//2 + 50):
                drawingList = functionsNormal('n')
                draw(drawingList)
            if(data.width//2 + 25 <= x <= data.width//2 + 300 and data.height//2 - 10 <= y <= data.height//2 + 50):
                drawingList = functionsNormal('m')
                draw(drawingList) 

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
            #call normal funct mode
        if(event.keysym == 'm'):
            drawingList = functionsNormal('m')
            draw(drawingList)
            #call mod arith mode
            
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

    if(data.mode == 'splashScreen'):
        canvas.create_text(data.width//2, data.height//4 + 25, 
                                text = "Welcome to Data Visualization",
                                    font = "Arial 26 bold")

        canvas.create_rectangle(data.width//2 - 300, data.height//2 - 10, data.width//2 - 25, data.height//2 + 50)
        canvas.create_text(data.width//2 - 170, data.height//2 + 20, text = "Functions", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 + 25, data.height//2 - 10, data.width//2 + 300, data.height//2 + 50)
        canvas.create_text(data.width//2 + 170, data.height//2 + 20, text = "Fractions", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 - 300, data.height//2 + 100, data.width//2 -25, data.height//2 + 160)
        canvas.create_text(data.width//2 - 170, data.height//2 + 130, text = "PI <3", font = "Arial 20 bold", fill = 'red')

        canvas.create_rectangle(data.width//2 + 25, data.height//2 + 100, data.width//2 + 300, data.height//2 + 160)
        canvas.create_text(data.width//2 + 170, data.height//2 + 130, text = "Free Style", font = "Arial 20 bold", fill = 'red')

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
        
        data.functionsPageLoaded = True

    if(data.mode == 'fractions'):
        canvas.create_image(400,400, image = data.fractionsBackground)
        canvas.create_text(data.width//2, data.height//4,
                                text = "Let us visualize fractions!",
                                    font = " Arial 24 bold")
        canvas.create_text(data.width//2, data.height//4 + 35,
                                text = "Click the fraction to start!",
                                    font = " Arial 24 bold")
        #canvas.create_rectangle(data.width//2 - 100, data.height//2 - 100, data.width//2 + 100, data.height//2 + 100)

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
    if(data.mode == 'freeDraw'):
        canvas.create_rectangle(data.width//2 - 137.5, data.height//2 - 30, data.width//2 + 137.5, data.height//2 + 30)
        canvas.create_text(data.width//2, data.height//2, text = "Free Style Drawing",
                                    font = 'Arial 20 bold', fill = 'red')

    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):                 # adapted from course notes
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
    print("bye!")

run(800, 800)