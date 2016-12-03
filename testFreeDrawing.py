import tkinter
import turtle

def freeDraw():
    root = tkinter.Tk()
    root.geometry("800x800+100+100")

    fr4 = tkinter.Frame(root, height=500, width=600, bd=4, bg="red", takefocus="", relief=tkinter.SUNKEN)

    fr4.grid(row=2, column=2, sticky=(tkinter.N, tkinter.E, tkinter.W, tkinter.S))

    # Canvas
    canvas = tkinter.Canvas(fr4, width=750, height=750)
    canvas.pack()

    # Turtle
    turtle1 = turtle.RawTurtle(canvas)
    turtle1.shape("circle")
    turtle1.penup()
    turtle1.setpos(-350,350)
    turtle1.write('Free Style Drawing')
    turtle1.home()
    turtle1.pendown()
    turtle1.color("black")
    
    def drag_handler(x, y):
        turtle1.ondrag(None)            # disable event inside event handler
        turtle1.goto(x, y)
        turtle1.ondrag(drag_handler)    # reenable event on event handler exit

    turtle1.ondrag(drag_handler)

    root.mainloop()

