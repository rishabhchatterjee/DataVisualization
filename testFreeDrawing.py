import turtle
import random


def freeDraw():

    def setup():
        turtle.shape('turtle')
        turtle.penup()
        turtle.setpos(-125,200)
        turtle.pendown()
        turtle.write("Click 'c' to change turtle colors!", font = 'Arial 20 bold')
        turtle.penup()
        turtle.setpos(0,0)

    def mouseClick(event):
        turtle.penup()
        turtle.goto(event.x-360,340-event.y)
        turtle.pendown()

    def draw(event):
        turtle.goto(event.x-360,340-event.y)

    def release(event):
        turtle.penup()

    def reset(event):
        turtle.clear()

    count = 0
    def changeColor(event):
        nonlocal count 
        count += 1
        colors = ['black','red','dark green','blue','orange','brown']
        turtle.color(colors[count%6])


    turtle.reset()
    turtle.speed(0)

    c=turtle.getcanvas()

    setup()
    c.bind("<Button-1>", mouseClick)
    c.bind("<B1-Motion>", draw)
    c.bind("<ButtonRelease-1>", release)
    c.bind("<Escape>",reset)
    c.bind("<c>", changeColor)


    s=turtle.Screen()
    s.title('FREE STYLE DRAWING')
    s.listen()

#freeDraw()