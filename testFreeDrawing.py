import turtle
import random
from testingScreenshot import *

def freeDraw():

    def setup():
        turtle.color('black')
        turtle.shape('circle')
        turtle.penup()
        turtle.setpos(-320,250)
        turtle.pendown()
        turtle.write("Click 'c' to change turtle colors!", font = 'Arial 12 bold')
        turtle.penup()
        turtle.setpos(-320, 230)
        turtle.pendown()
        turtle.write("Click 'e' for eraser!", font = 'Arial 12 bold')
        turtle.penup()
        turtle.setpos(-320, 210)
        turtle.pendown()
        turtle.write("Click 'esc' to clear screen!", font = 'Arial 12 bold')
        turtle.penup()
        turtle.setpos(-320, 190)
        turtle.pendown()
        turtle.write("Click 'd' to go back to drawing mode from eraser!", font = 'Arial 12 bold')
        turtle.penup()
        turtle.setpos(-320, 170)
        turtle.pendown()
        turtle.write("Click 's' to take Screenshot!", font = 'Arial 12 bold')
        turtle.penup()
        turtle.setpos(0,0)

    def mousePressed(event):
        turtle.penup()
        turtle.goto(event.x-360,340-event.y)
        turtle.pendown()

    def draw(event):
        turtle.goto(event.x-360,340-event.y)

    def mouseReleased(event):
        turtle.penup()

    def clearScreen(event):
        turtle.clear()
        setup()

    count = 0
    def changeColor(event):
        nonlocal count 
        turtle.pensize(1)
        count += 1
        colors = ['black','red','dark green','blue','orange','hot pink']
        turtle.color(colors[count%6])

    def eraser(event):
        turtle.pensize(12)
        turtle.color('white')
        turtle.shape('circle')
        nonlocal count
        count -= 1

    def screenshot(event):
        takeScreenshotFreeDraw()

    turtle.reset()
    turtle.speed(0)

    canvas=turtle.getcanvas()
    setup()

    canvas.bind("<Button-1>", mousePressed)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", mouseReleased)
    canvas.bind("<Escape>",clearScreen)
    canvas.bind("<c>", changeColor)
    canvas.bind("<e>", eraser)
    canvas.bind("<d>", changeColor)
    canvas.bind("<s>", screenshot)
    
    screen=turtle.Screen()
    screen.title('FREE STYLE DRAWING')
    screen.listen()

#freeDraw()