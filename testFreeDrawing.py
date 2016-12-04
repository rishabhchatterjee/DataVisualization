import turtle


def freeDraw():
    
    turtle.shape('circle')

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

    turtle.reset()
    turtle.speed(0)

    c=turtle.getcanvas()

    c.bind("<Button-1>", mouseClick)
    c.bind("<B1-Motion>", draw)
    c.bind("<ButtonRelease-1>", release)
    c.bind("<Escape>",reset)


    s=turtle.Screen()
    s.title('FREE STYLE DRAWING')
    s.listen()

#freeDraw()