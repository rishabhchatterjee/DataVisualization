# events-example0.py
# Barebones timer, mouse, and keyboard events
from functionsNormal import functionsNormal
from fractions import *
from piDigits import *
from draw import *
from tkinter import *

####################################
# customize these functions
####################################
def init(data):
    data.mode = 'splashScreen'
    data.background = PhotoImage(file = 'mathstats.gif')
    data.functionsBackground = PhotoImage(file = 'Functions.gif')
    data.fractionsBackground = PhotoImage(file = 'f.gif')
    data.piBackground = PhotoImage(file = 'PI.gif')

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if(data.mode == 'splashScreen'):
        if(event.keysym == 'f'):
            data.mode = 'functions'
        elif(event.keysym == 'q'):
            data.mode = 'fractions'
        elif(event.keysym == 'p'):
            data.mode = 'pi'

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
def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(400,400, image = data.background)

    if(data.mode == 'splashScreen'):
        canvas.create_text(data.width//2, data.height//4 + 25, 
                                text = "Welcome to Data Visualization",
                                    font = "Arial 26 bold")
        canvas.create_text(data.width//2, data.height//2, 
                            text = 'Press \'f\' for function mode\n\nPress \'q\' for fraction mode\n\nPress \'p\' for Pi mode',
                                font = "Arial 24 bold")
         
    if(data.mode == 'functions'):
        canvas.create_image(400,275, image = data.functionsBackground)
        canvas.create_text(data.width//2, data.height//4, 
                                text = "Let us visualize functions!",
                                    font = "Arial 26 bold")
        canvas.create_text(data.width//2, data.height//2, 
                    text = 'Press \'n\' for number mode\n\nPress \'m\' for modular arithmetic mode',
                        font = "Arial 24 bold") 

    if(data.mode == 'fractions'):
        canvas.create_image(400,400, image = data.fractionsBackground)
        canvas.create_text(data.width//2, data.height//4,
                                text = "Let us visualize fractions!",
                                    font = " Arial 24 bold")
        canvas.create_text(data.width//2, data.height//4 + 35,
                                text = "Press Space to start!",
                                    font = " Arial 24 bold")
    if(data.mode == 'pi'):
        canvas.create_image(400,500, image = data.piBackground)
        canvas.create_text(data.width//2, data.height//5,
                                text = "Let us visualize Pi!",
                                    font = " Arial 24 bold")
        canvas.create_text(data.width//2, data.height//3, 
                    text = 'Press \'c\' for Chudnovsky Algorithm\n\nPress \'r\' for recursive algorithm (Error ~10^-7)',
                        font = "Arial 24 bold") 


    


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