import pyscreenshot as ImageGrab
from tkinter import simpledialog

def takeScreenshot():                                   
    im = ImageGrab.grab(bbox = (290,50,1075,720))
    name = simpledialog.askstring(" ", "Save file as")
    im.save(name + '.jpg')

def takeScreenshotFreeDraw():                           # for freeDraw mode
    im = ImageGrab.grab(bbox = (350,100,1025,700))
    name = simpledialog.askstring(" ", "Save file as")
    im.save(name + '.jpg')

