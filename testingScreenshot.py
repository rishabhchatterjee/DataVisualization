import pyscreenshot as ImageGrab

def takeScreenshot():
    im = ImageGrab.grab(bbox = (290,50,1075,1450))
    im.save('dataVisualization.jpg')
#takeScreenshot()