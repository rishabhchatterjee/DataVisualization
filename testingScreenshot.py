import pyscreenshot as ImageGrab
from tkinter import simpledialog

def takeScreenshot():
    im = ImageGrab.grab(bbox = (290,50,1075,1450))
    name = simpledialog.askstring(" ", "Save file as")
    im.save(name + '.jpg')
#takeScreenshot()